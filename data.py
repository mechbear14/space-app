from PIL import Image, ImageTk
from math import fabs


class FilteredXML:
    def __init__(self, xml):
        self.elev = xml.get("elev")
        self.lat = float(xml.get("lat"))
        self.lon = float(xml.get("lon"))
        self.owner = xml.get("owner")
        self.name = xml.get("name")


class Map:
    def __init__(self, canvas, image_path, route_path, buoys):
        self.image = Image.open(image_path)
        self.width = self.image.width
        self.height = self.image.height
        self.route_map = Image.open(route_path)
        self.offset = self.image.width / 4
        self.buoys = buoys
        self.showing_route = False
        self.canvas = canvas
        self.w = 960
        self.h = 540

        self.translate = [0, 0]
        self.current_location = [0, 0]
        self.temp_translate = [0, 0]
        self.scale = 3.0

        self.image_tk = ImageTk.PhotoImage(
            self.image.resize((round(self.image.width * self.scale), round(self.image.height * self.scale)), Image.ANTIALIAS)
        )
        self.route_tk = ImageTk.PhotoImage(
            self.route_map.resize((round(self.route_map.width * self.scale), round(self.route_map.height * self.scale)), Image.ANTIALIAS)
        )
        self.image_ref = self.canvas.create_image((960 / 2, 540 / 2), image=self.image_tk)

    def mark_start(self, x, y):
        self.current_location = [x, y]

    def move(self, x, y):
        self.temp_translate = [x - self.current_location[0],
                               y - self.current_location[1]]
        self.canvas.coords(self.image_ref, (self.w / 2 + self.translate[0] + self.temp_translate[0],
                                            self.h / 2 + self.translate[1] + self.temp_translate[1]))

    def end_drag(self):
        self.translate = [self.translate[0] + self.temp_translate[0],
                          self.translate[1] + self.temp_translate[1]]
        self.temp_translate = [0, 0]
        self.current_location = [0, 0]

    def scale_up(self, event):
        self.scale += 0.1
        factor = self.scale / (self.scale + 0.1)
        self.canvas.scale(self.image_ref, event.x, event.y, factor, factor)

    def scale_down(self, event):
        self.scale -= 0.1
        factor = self.scale / (self.scale + 0.1)
        self.canvas.scale(self.image_ref, event.x, event.y, factor, factor)

    def show_route(self, show_route):
        if show_route:
            self.canvas.itemconfig(self.image_ref, image=self.route_tk)
        else:
            self.canvas.itemconfig(self.image_ref, image=self.image_tk)

    def render(self):
        for b in self.buoys:
            b.render(self.canvas)


class BuoyPoint:
    def __init__(self, buoy_xml, map_object):
        self.buoy_xml = buoy_xml
        self.x = ((buoy_xml.lon + 180) / 360 * map_object.width + map_object.offset) % map_object.width
        self.y = ((buoy_xml.lat + 90) / 180 * map_object.height) % map_object.height
        self.ref = None
        self.card_ref = None

    def render(self, canvas):
        self.ref = canvas.create_oval((self.x - 5, self.y - 5, self.x + 5, self.y + 5), fill="yellow")

    def render_card(self, canvas):
        self.card_ref = canvas.create_rectangle((self.x + 10, self.y, 200, 50), fill="white")

    def is_in_point(self, x, y):
        return fabs(x - self.x) < 5 and fabs(y - self.y) < 5
