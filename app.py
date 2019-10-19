# A bear has changed it
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
        self.draw_boats_box = tk.Frame(master)
        self.draw_fishing_box = tk.Frame(master)
        self.draw_freq_box = tk.Frame(master)
        self.draw_buoys_box = tk.Frame(master)

        self.draw_boats_var = tk.BooleanVar(self.draw_boats_box, False)
        self.draw_fishing_var = tk.BooleanVar(self.draw_fishing_box, False)
        self.draw_freq_var = tk.BooleanVar(self.draw_freq_box, False)
        self.draw_buoys_var = tk.BooleanVar(self.draw_buoys_box, False)

        self.draw_boats_checkbox = tk.Checkbutton(self.draw_boats_box, variable=self.draw_boats_var)
        self.draw_fishing_checkbox = tk.Checkbutton(self.draw_fishing_box, variable=self.draw_fishing_var)
        self.draw_freq_checkbox = tk.Checkbutton(self.draw_freq_box, variable=self.draw_freq_var)
        self.draw_buoys_checkbox = tk.Checkbutton(self.draw_buoys_box, variable=self.draw_buoys_var)
        self.draw_boats_checkbox.pack(side=tk.LEFT)
        self.draw_fishing_checkbox.pack(side=tk.LEFT)
        self.draw_freq_checkbox.pack(side=tk.LEFT)
        self.draw_buoys_checkbox.pack(side=tk.LEFT)

        self.draw_boats_label = tk.Label(self.draw_boats_box, text="Boats")
        self.draw_fishing_label = tk.Label(self.draw_fishing_box, text="Fishing boats")
        self.draw_freq_label = tk.Label(self.draw_freq_box, text="Frequent routes")
        self.draw_buoys_label = tk.Label(self.draw_buoys_box, text="Buoys")
        self.draw_boats_label.pack(side=tk.LEFT)
        self.draw_fishing_label.pack(side=tk.LEFT)
        self.draw_freq_label.pack(side=tk.LEFT)
        self.draw_buoys_label.pack(side=tk.LEFT)

        self.draw_boats_box.pack(side=tk.TOP, fill=tk.X)
        self.draw_fishing_box.pack(side=tk.TOP, fill=tk.X)
        self.draw_freq_box.pack(side=tk.TOP, fill=tk.X)
        self.draw_buoys_box.pack(side=tk.TOP, fill=tk.X)


class App:
    def __init__(self, master):
        self.left_pane = tk.Frame(master)
        self.left_pane.pack(side=tk.LEFT)
        self.canvas_pane = tk.Frame(master)
        self.canvas_pane.pack(side=tk.LEFT)

        self.filters = Filter(self.left_pane)
        self.canvas = Display(self.canvas_pane)


root = tk.Tk()
app = App(root)
root.mainloop()
