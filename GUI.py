def main():
    import tkinter as tk
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    # Window set up
    window = tk.Tk()
    window.title("Differential Equation Visualizer and Solver")
    window.geometry("800x600")
    window.resizable(width=False, height=False)

    # Data
    x = [1, 2, 3, 4, 5]
    y = [2, 5, 3, 6, 4]

    # Draw graph
    def drawChart():
        fig.clear()
        fig.add_subplot().plot(x, y)
        canvas.draw_idle()

    # Graph inputted points
    def graphInput():
        inputString = pointInput.get()
        parts = inputString.split(",")
        if parts:
            number_x = parts[0].split()
            number_y = parts[1].split()
            for num_str in number_x:
                try:
                    number = int(num_str)
                    x.append(number)
                    pointList_x.insert(tk.END, number)
                except ValueError:
                    pass  # Ignore non-numeric values
            for num_str in number_y:
                try:
                    number = int(num_str)
                    y.append(number)
                    pointList_y.insert(tk.END, number)
                except ValueError:
                    pass  # Ignore non-numeric values
        pointInput.delete(0, 'end')
        drawChart()

    # Graph initialization
    fig, ax = plt.subplots()
    ax.plot(x, y)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()

    # Close window
    windowClose = tk.Button(master=window, text="Close Application", command=window.destroy)

    # Input points
    frm_entry = tk.Frame(master=window)
    pointInput = tk.Entry(master=frm_entry, bg="white", fg="black")
    pointButton = tk.Button(master=frm_entry, text="Enter a point", command=graphInput)

    pointInput.grid(row=0, column=0, sticky="e")
    pointButton.grid(row=0, column=1, sticky="w")

    # Point list
    pointList_x = tk.Listbox(master=window, width=5)
    pointList_y = tk.Listbox(master=window, width=5)

    for item in x:
        pointList_x.insert(tk.END, item)
    for item in y:
        pointList_y.insert(tk.END, item)

    # Widgets placement
    canvas_widget.grid(row=0, column=0, rowspan=2, columnspan=3, padx=10, pady=10)
    windowClose.grid(row=2, column=4, padx=10, pady=10, sticky="e")
    frm_entry.grid(row=2, column=0, rowspan=2, padx=10, sticky="w")
    pointList_x.grid(row=0, column=3, padx=10, pady=10)
    pointList_y.grid(row=0, column=4, padx=10, pady=10)

    # Configure row weights to make them expandable
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.rowconfigure(2, weight=0)
    window.rowconfigure(3, weight=0)
    window.rowconfigure(4, weight=0)
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=1)

    # Window main loop
    window.mainloop()


if __name__ == "__main__":
    main()
