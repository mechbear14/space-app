from bs4 import BeautifulSoup
import requests
import tkinter as tk
from data import Map, FilteredXML, BuoyPoint


class Display:
    def __init__(self, master, buoy_data):
        self.canvas = tk.Canvas(master, width=960, height=540, background="black")
        self.canvas.pack()
        self.translate = [0, 0]
        self.current_location = [0, 0]
        self.temp_translate = [0, 0]
        self.scale = 1
        self.drawing = []
        self.dragging = False

        self.buoys = map(lambda b: BuoyPoint(b, self.map), buoy_data)
        self.map = Map(self.canvas, "map1.png", "map2.png", self.buoys)
        self.map.render()
        global map_object
        map_object = self.map

        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<Button-4>", self.on_scroll_up)
        self.canvas.bind("<Button-5>", self.on_scroll_down)

    def on_mouse_down(self, event):
        self.dragging = True
        self.canvas.bind("<B1-Motion>", self.on_mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
        self.map.mark_start(event.x, event.y)

    def on_mouse_move(self, event):
        self.map.move(event.x, event.y)
        # pass

    def on_mouse_up(self, event):
        self.map.end_drag()
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

    def on_scroll_down(self, event):
        self.map.scale_down(event)

    def on_scroll_up(self, event):
        self.map.scale_up(event)


class Filter:
    def __init__(self, master):
        self.draw_boats_var = tk.BooleanVar()
        self.draw_fishing_var = tk.BooleanVar()
        self.draw_freq_var = tk.BooleanVar()
        self.draw_buoys_var = tk.BooleanVar()

        self.draw_boats_checkbox = tk.Checkbutton(master, anchor=tk.W, text="Boats", variable=self.draw_boats_var)
        self.draw_fishing_checkbox = tk.Checkbutton(master, anchor=tk.W, text="Fishing boats", variable=self.draw_fishing_var)
        self.draw_freq_checkbox = tk.Checkbutton(master, anchor=tk.W, text="Frequent routes", variable=self.draw_freq_var, command=self.update)
        self.draw_buoys_checkbox = tk.Checkbutton(master, anchor=tk.W, text="Buoys", variable=self.draw_buoys_var)
        self.draw_boats_checkbox.pack(fill=tk.X)
        self.draw_fishing_checkbox.pack(fill=tk.X)
        self.draw_freq_checkbox.pack(fill=tk.X)
        self.draw_buoys_checkbox.pack(fill=tk.X)

    def update(self):
        map_object.show_route(self.draw_freq_var.get())


class App:
    def __init__(self, master, data):
        self.left_pane = tk.Frame(master)
        self.left_pane.pack(side=tk.LEFT)
        self.canvas_pane = tk.Frame(master)
        self.canvas_pane.pack(side=tk.LEFT)

        self.filters = Filter(self.left_pane)
        self.canvas = Display(self.canvas_pane, data)


def start():
    r = requests.get("https://ndbc.noaa.gov/activestations.xml")
    soup = BeautifulSoup(r.text)
    buoy_soup = soup.find_all(type="buoy")
    buoy_list = list(map(lambda b: FilteredXML(b), buoy_soup))

    root = tk.Tk()
# <<<<<<< HEAD
#     app = App(root, buoy_list)
#     root.title("Bear's space app")
# =======
#     app = App(root)
#     root.title("IOS - Internet over the Oceans")
# >>>>>>> b1da2dd4948f03c1435ef86728ef93af195e83ea
    root.update()
    root.mainloop()


if __name__ =="__main__":
    start()
