from PIL import Image, ImageTk


class Map:
    def __init__(self, image_path):
        self.path = image_path
        self.image = Image.open(image_path)
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.image_ref = None

        self.translation = [0, 0]
        self.scale = 1.0

    def render(self, canvas):
        w, h = canvas.winfo_width(), canvas.winfo_height()
        self.image_ref = canvas.create_image((w / 2, h / 2), self.image_tk)
        canvas.scale(self.image_ref, w / 2, h / 2, 3, 3)

    def move(self, x, y):
        pass

    def scale_up(self):
        pass

    def scale_down(self):
        pass
