import tkinter as tk


def start():
    class Display:
        def __init__(self, master):
            self.canvas = tk.Canvas(master, width=960, height=540, background="black")
            self.canvas.pack()
            self.translate = [0, 0]
            self.current_location = [0, 0]
            self.temp_translate = [0, 0]
            self.scale = 1
            self.drawing = []
            self.dragging = False

            self.canvas.bind("<Button-1>", self.on_mouse_down)

            # Test
            self.circle = self.canvas.create_oval((460, 250, 500, 290), fill="yellow")

        def on_mouse_down(self, event):
            self.dragging = True
            self.canvas.bind("<B1-Motion>", self.on_mouse_move)
            self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
            self.current_location = [event.x, event.y]

        def on_mouse_move(self, event):
            self.temp_translate = [event.x - self.current_location[0],
                                   event.y - self.current_location[1]]
            self.canvas.coords(self.circle, (460 + self.translate[0] + self.temp_translate[0],
                                             250 + self.translate[1] + self.temp_translate[1],
                                             500 + self.translate[0] + self.temp_translate[0],
                                             290 + self.translate[1] + self.temp_translate[1]))

        def on_mouse_up(self, event):
            self.translate = [self.translate[0] + self.temp_translate[0],
                              self.translate[1] + self.temp_translate[1]]
            # print(self.translate)
            self.temp_translate = [0, 0]
            self.current_location = [0, 0]
            self.canvas.unbind("<B1-Motion>")
            self.canvas.unbind("<ButtonRelease-1>")

        def on_scroll_down(self, event):
            pass

        def on_scroll_up(self, event):
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

