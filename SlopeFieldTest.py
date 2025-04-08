import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def slope_field(f, x_range, y_range, step=0.2):
    x, y = np.meshgrid(np.arange(x_range[0], x_range[1], step),
                       np.arange(y_range[0], y_range[1], step))
    u = np.ones_like(x)
    v = f(x, y)
    norm = np.sqrt(u**2 + v**2)
    return x, y, u/norm, v/norm

def plot_slope_field(f, x_range, y_range, ax):
    x, y, u, v = slope_field(f, x_range, y_range)
    ax.quiver(x, y, u, v, color='r', headwidth=3, headlength=5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Slope Field')
    ax.set_xlim(x_range)
    ax.set_ylim(y_range)
    ax.grid(True)

def main():
    root = tk.Tk()
    root.title("Slope Field Plotter")

    equation_label = tk.Label(root, text="Enter dy/dx as a function of x and y (e.g., x*y, np.sin(x) + y**2):")
    equation_label.pack()
    equation_entry = tk.Entry(root, width=50)
    equation_entry.pack()
    equation_entry.insert(0, "x - y")

    x_min_label = tk.Label(root, text="Enter x range (min):")
    x_min_label.pack()
    x_min_entry = tk.Entry(root, width=10)
    x_min_entry.pack()
    x_min_entry.insert(0, "-5")

    x_max_label = tk.Label(root, text="Enter x range (max):")
    x_max_label.pack()
    x_max_entry = tk.Entry(root, width=10)
    x_max_entry.pack()
    x_max_entry.insert(0, "5")

    y_min_label = tk.Label(root, text="Enter y range (min):")
    y_min_label.pack()
    y_min_entry = tk.Entry(root, width=10)
    y_min_entry.pack()
    y_min_entry.insert(0, "-5")

    y_max_label = tk.Label(root, text="Enter y range (max):")
    y_max_label.pack()
    y_max_entry = tk.Entry(root, width=10)
    y_max_entry.pack()
    y_max_entry.insert(0, "5")

    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    def plot():
        try:
            equation_str = equation_entry.get()
            f = lambda x, y: eval(equation_str)
            x_range = (float(x_min_entry.get()), float(x_max_entry.get()))
            y_range = (float(y_min_entry.get()), float(y_max_entry.get()))

            ax.clear()
            plot_slope_field(f, x_range, y_range, ax)
            canvas.draw()
        except Exception as e:
             print(f"Error: {e}")
             tk.messagebox.showerror("Error", f"Invalid input: {e}")

    plot_button = tk.Button(root, text="Plot", command=plot)
    plot_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
