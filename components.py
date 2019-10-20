from tkinter import Checkbutton, Canvas, Tk, Frame
from bs4 import BeautifulSoup
import requests
from element import Map


class App:
    def __init__(self, master, map_object):
        self.canvas = Canvas(master, width=960, height=540, background="black")
        self.canvas.pack()
        self.translate = [0, 0]
        self.current_location = [0, 0]
        self.temp_translate = [0, 0]
        self.scale = 30
        self.map_object = map_object
        self.map_object.render(self.canvas)

        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<Button-4>", self.on_scroll_up)
        self.canvas.bind("<Button-5>", self.on_scroll_down)

    def on_mouse_down(self, event):
        self.canvas.bind("<B1-Motion>", self.on_mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
        self.current_location = [event.x, event.y]

    def on_mouse_move(self, event):
        self.temp_translate = [event.x - self.current_location[0],
                               event.y - self.current_location[1]]
        self.map_object.move(self.canvas,
                             self.temp_translate[0] + self.translate[0],
                             self.temp_translate[1] + self.translate[1])

    def on_mouse_up(self, event):
        self.translate = [self.translate[0] + self.temp_translate[0],
                          self.translate[1] + self.temp_translate[1]]
        self.temp_translate = [0, 0]
        self.current_location = [0, 0]
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

    def on_scroll_down(self, event):
        self.scale -= 1
        self.map_object.scale(self.canvas, event.x, event.y, self.scale / 10)

    def on_scroll_up(self, event):
        self.scale += 1
        self.map_object.scale(self.canvas, event.x, event.y, self.scale / 10)


root = Tk()
r = requests.get("https://ndbc.noaa.gov/activestations.xml")
soup = BeautifulSoup(r.text, "lxml")
buoy_soup = soup.find_all("station")
map_object = Map("map1.png", "map2.png", buoy_soup)
app = App(root, map_object)
root.mainloop()
# class Display:
#     def __init__(self, master):
#         self.canvas = Canvas(master, width=960, height=540, background="black")
#         self.canvas.pack()
#         self.translate = [0, 0]
#         self.current_location = [0, 0]
#         self.temp_translate = [0, 0]
#         self.scale = 1
#         self.drawing = []
#         self.dragging = False
#
#         # self.buoys = map(lambda b: BuoyPoint(b, self.map), buoy_data)
#         # self.map = Map(self.canvas, "map1.png", "map2.png", self.buoys)
#         # self.map.render()
#         # global map_object
#         # map_object = self.map
#         r = requests.get("https://ndbc.noaa.gov/activestations.xml")
#         soup = BeautifulSoup(r.text, "lxml")
#         buoy_soup = soup.find_all(type="buoy")
#         self.map_object = Map("map1.png", "map2.png", buoy_soup)
#
#         self.canvas.bind("<Button-1>", self.on_mouse_down)
#         self.canvas.bind("<Button-4>", self.on_scroll_up)
#         self.canvas.bind("<Button-5>", self.on_scroll_down)
#
#     def on_mouse_down(self, event):
#         self.dragging = True
#         self.canvas.bind("<B1-Motion>", self.on_mouse_move)
#         self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
#         self.map.mark_start(event.x, event.y)
#
#     def on_mouse_move(self, event):
#         self.map.move(event.x, event.y)
#         # pass
#
#     def on_mouse_up(self, event):
#         self.map.end_drag()
#         self.canvas.unbind("<B1-Motion>")
#         self.canvas.unbind("<ButtonRelease-1>")
#
#     def on_scroll_down(self, event):
#         self.map.scale_down(event)
#
#     def on_scroll_up(self, event):
#         self.map.scale_up(event)
