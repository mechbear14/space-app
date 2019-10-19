import tkinter as tk


class Display:
    def __init__(self, master):
        self.canvas = tk.Canvas(master, width=960, height=540)
        self.canvas.pack()
        self.pan = [0, 0]
        self.drawing = []

    def on_drag(self, event):
        pass

    def on_scroll(self, event):
        pass


class Filter:
    def __init__(self, master):
        self.draw_boats = tk.BooleanVar(master, False)
        self.draw_fishing = tk.BooleanVar(master, False)
        self.draw_freq = tk.BooleanVar(master, False)
        self.draw_buoys = tk.BooleanVar(master, False)
