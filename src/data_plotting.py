import tkinter

# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

# style.use('seaborn-whitegrid')

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)


class IMUPlot:
    def __init__(self):
        self.x = []
        self.y = []

        # making figure with data
        self.fig = fig
        self.ax = ax

        # make tkinter plot
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        self.toolbar = NavigationToolbar2Tk(self.canvas, root)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, self.canvas, self.toolbar)

        def _quit():
            # root.quit()  # stops mainloop
            root.destroy()

        self.canvas.mpl_connect("key_press_event", on_key_press)

        button = tkinter.Button(master=root, text="Quit", command=_quit)
        button.pack(side=tkinter.BOTTOM)

        self._update_tkinter_app()

    @staticmethod
    def _update_tkinter_app():
        root.update_idletasks()
        root.update()

    def add_data_point(self, x, y):
        self.ax.clear()
        self.x.append(x)
        self.y.append(y)
        self.ax.plot(self.x, self.y)
        self.canvas.draw()

        self._update_tkinter_app()


# tkinter.mainloop()
