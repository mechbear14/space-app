from tkinter import Checkbutton, Canvas, Tk, Frame, X, W, LEFT
from bs4 import BeautifulSoup
import requests
from element import Map


class Display:
    def __init__(self, master, map_object):
        self.canvas = Canvas(master, width=960, height=540, background="black")
        self.canvas.pack()
        self.translate = [0, 0]
        self.current_location = [0, 0]
        self.temp_translate = [0, 0]
        self.scale = 30
        self.map_object = map_object
        self.map_object.render(self.canvas)
        self.map_object.scale(self.canvas, 0, 0, self.scale / 10)

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
        self.map_object.scale(self.canvas, self.translate[0], self.translate[1], self.scale / 10)

    def on_scroll_up(self, event):
        self.scale += 1
        self.map_object.scale(self.canvas, self.translate[0], self.translate[1], self.scale / 10)


class Filter:
    def __init__(self, master, map_object):
        self.canvas = None
        self.map_object = map_object
        self.draw_freq_checkbox = Checkbutton(master, anchor=W, text="Frequent routes",
                                              variable=self.map_object.show_route, command=self.update_map)
        self.draw_buoys_checkbox = Checkbutton(master, anchor=W, text="Buoys",
                                               variable=self.map_object.show_buoys, command=self.update_buoy)
        self.draw_freq_checkbox.pack(fill=X)
        self.draw_buoys_checkbox.pack(fill=X)

    def set_control_canvas(self, canvas):
        self.canvas = canvas

    def update_map(self):
        if self.map_object.show_route.get():
            self.map_object.set_image("route", self.canvas.canvas)
        else:
            self.map_object.set_image("map", self.canvas.canvas)

    def update_buoy(self):
        self.map_object.set_buoys(self.canvas.canvas, self.map_object.show_buoys.get(), self.canvas.translate)

class App:
    def __init__(self, master, data):
        self.left_pane = Frame(master)
        self.left_pane.pack(side=LEFT)
        self.canvas_pane = Frame(master)
        self.canvas_pane.pack(side=LEFT)

        self.filters = Filter(self.left_pane, map_object)
        self.canvas = Display(self.canvas_pane, data)
        self.filters.set_control_canvas(self.canvas)

def start():   
    root = Tk()
    r = requests.get("https://ndbc.noaa.gov/activestations.xml")
    soup = BeautifulSoup(r.text, "lxml")
    buoy_soup = soup.find_all("station")
    global map_object
    map_object = Map("map1.png", "map2.png", buoy_soup)
    app = App(root, map_object)
    root.mainloop()

if __name__ =="__main__":
    start()
