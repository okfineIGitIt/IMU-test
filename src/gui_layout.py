import tkinter as tk

window = tk.Tk()


render_frame = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)
render_label = tk.Label(master=render_frame, text=f"Row {1}\nColumn {1}")

graph_frame = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)
graph_label = tk.Label(master=graph_frame, text=f"Row {1}\nColumn {2}")

control_frame = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)
control_label = tk.Label(master=control_frame, text=f"Row {2}\nColumn {1}")

monitor_frame = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)
monitor_label = tk.Label(master=monitor_frame, text=f"Row {2}\nColumn {2}")

window.columnconfigure(1, weight=1, minsize=75)
window.rowconfigure(1, weight=1, minsize=50)
window.columnconfigure(2, weight=1, minsize=75)
window.rowconfigure(2, weight=1, minsize=50)

render_label.pack(padx=30, pady=30)
graph_label.pack(padx=30, pady=30)
control_label.pack(padx=30, pady=30)
monitor_label.pack(padx=30, pady=30)

render_frame.grid(row=1, column=1)
graph_frame.grid(row=1, column=2)
control_frame.grid(row=2, column=1)
monitor_frame.grid(row=2, column=2)

window.mainloop()
