import tkinter as tk
from PIL import Image, ImageTk


class Map:
    def __init__(self, image_path, canvas):
        self.path = image_path
        self.image = Image.open(image_path)
        self.image = self.image.resize((self.image.width * 3, self.image.height * 3), Image.ANTIALIAS)
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.canvas = canvas
        self.w, self.h = self.canvas.winfo_width(), canvas.winfo_height()
        self.image_ref = canvas.create_image((self.w / 2, self.h / 2), image=self.image_tk)

        self.translate = [0, 0]
        self.current_location = [0, 0]
        self.temp_translate = [0, 0]
        self.scale = 1.0

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
