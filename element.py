from PIL import Image, ImageTk
from tkinter import BooleanVar


class MapImage:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.scaled_image = self.image
        self.width = self.image.width
        self.height = self.image.height
        self.image_tk = ImageTk.PhotoImage(self.scaled_image)

    def render(self, canvas, image_ref, x, y, scale):
        self.image = self.image.resize((self.width * scale, self.height * scale), Image.ANTIALIAS)
        canvas.itemconfig(image_ref, image=self.image_tk)
        canvas.coords(image_ref, (x, y))

    def resize(self, scale):
        self.scaled_image = self.image.resize((round(self.image.width * scale), round(self.image.height * scale)))
        self.image_tk = ImageTk.PhotoImage(self.scaled_image)


class BuoyMark:
    def __init__(self, xml, map_image):
        self.elev = xml.get("elev")
        self.lat = float(xml.get("lat"))
        self.lon = float(xml.get("lon"))
        self.owner = xml.get("owner")
        self.name = xml.get("name")
        self.x = ((self.lon + 180) / 360 * map_image.width) % map_image.width - map_image.width / 2
        self.y = ((90 - self.lat) / 180 * map_image.height + 66.7) % map_image.height - map_image.height / 2
        self.scaled_x = self.x
        self.scaled_y = self.y

    def render(self, canvas, ref, x, y, scale):
        canvas.scale(ref, x, y, scale, scale)


class Map:
    def __init__(self, map_path, route_path, buoy_xml):
        self.background_map = MapImage(map_path)
        self.route_map = MapImage(route_path)
        self.buoys = list(map(lambda b: BuoyMark(b, self.background_map), buoy_xml))
        self.show_route = BooleanVar()
        self.show_buoys = BooleanVar()
        self.image_ref = None
        self.buoys_ref = []

    def render(self, canvas):
        # global_offset_x = self.background_map.width / 2
        # global_offset_y = self.background_map.height / 2
        self.image_ref = canvas.create_image((0, 0), image=self.background_map.image_tk)
        # for b in self.buoys:
        #     self.buoys_ref.append(canvas.create_oval((b.x - 5, b.y - 5, b.x + 5, b.y + 5), fill="yellow"))
        # print(self.buoys_ref)

    def move(self, canvas, dx, dy):
        canvas.coords(self.image_ref, (dx, dy))
        for id, b in enumerate(self.buoys_ref):
            canvas.coords(b, (self.buoys[id].scaled_x - 5 + dx, self.buoys[id].scaled_y - 5 + dy, self.buoys[id].scaled_x + 5 + dx, self.buoys[id].scaled_y + 5 + dy))

    def scale(self, canvas, mx, my, s):
        self.background_map.resize(s)
        self.route_map.resize(s)
        canvas.itemconfig(self.image_ref, image=self.background_map.image_tk)
        if len(self.buoys_ref) > 0:
            for id, b in enumerate(self.buoys_ref):
                x = self.buoys[id].x
                y = self.buoys[id].y
                self.buoys[id].scaled_x = s * x
                self.buoys[id].scaled_y = s * y
                canvas.coords(self.buoys_ref[id], (self.buoys[id].scaled_x - 5 + mx, self.buoys[id].scaled_y - 5 + my,
                                                   self.buoys[id].scaled_x + 5 + mx, self.buoys[id].scaled_y + 5 + my))
        else:
            for id, b in enumerate(self.buoys):
                x = self.buoys[id].x
                y = self.buoys[id].y
                self.buoys[id].scaled_x = s * x
                self.buoys[id].scaled_y = s * y

    def set_image(self, image, canvas):
        if image == "route":
            canvas.itemconfig(self.image_ref, image=self.route_map.image_tk)
        elif image == "map":
            canvas.itemconfig(self.image_ref, image=self.background_map.image_tk)

    def set_buoys(self, canvas, show, translate):
        if show:
            for b in self.buoys:
                self.buoys_ref.append(canvas.create_oval((b.scaled_x + translate[0] - 5,
                                                          b.scaled_y + translate[1] - 5,
                                                          b.scaled_x + translate[0] + 5,
                                                          b.scaled_y + translate[1] + 5), fill="yellow"))
        else:
            for b in self.buoys_ref:
                canvas.delete(b)
            self.buoys_ref.clear()
