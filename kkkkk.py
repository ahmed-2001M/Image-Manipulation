import Tkinter as tk
import ttk
##loading matplotlib modules
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import numpy as np

top = tk.Tk()
top.title("Intermolecular PDFs")

top_frame = ttk.Frame(top, padding = (10, 10))
top_frame.pack()

matplotlib.rcParams["xtick.labelsize"] = 11
matplotlib.rcParams["ytick.labelsize"] = 11

fig = Figure(figsize=(10, 6), dpi=100) ##create a figure; modify the size here

x = np.linspace(0,1)
y = np.sin(x)
z = np.cos(x)

ax = fig.add_subplot(211)

ax.set_title("Individual PDFs")
# ax.set_xlabel(ur"r (\u00c5)", labelpad = 3, fontsize = 15)
# ax.set_ylabel(ur"PDF, G (\u00c5$^{-2})$", labelpad = 10, fontsize = 15)
line, = ax.plot(x,y, "r-", lw=2)

ax2 = fig.add_subplot(212)

ax2.set_title("Difference PDFs")
# ax2.set_xlabel(ur"r (\u00c5)", labelpad = 3, fontsize = 15)
# ax2.set_ylabel(ur"PDF, G (\u00c5$^{-2})$", labelpad = 10, fontsize = 15)
line2, = ax2.plot(x,z,"g-", lw=2)

canvas = FigureCanvasTkAgg(fig, master = top_frame)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

fig.tight_layout()

toolbar = NavigationToolbar2TkAgg(canvas, top_frame)
toolbar.update()
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def update():
    new_x = np.linspace(1,100)
    new_y = new_x**2
    new_z = new_x**3

    line.set_data(new_x,new_y)
    line2.set_data(new_x,new_z)

    ax.relim()
    ax.autoscale()
    ax2.relim()
    ax2.autoscale()
    fig.tight_layout()
    canvas.draw_idle()
    toolbar.update()

ttk.Button(top_frame, text = "update",command = update).pack()


top.mainloop()