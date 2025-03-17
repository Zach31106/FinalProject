import tkinter as tk

#from tkinter import * (used for scrollbar implementation)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


def showButtons(frame):
    frame.grid(row=1, column=0)
    frame.update_idletasks()

def hideButtons(frame):
    frame.grid_remove()

def deleteText(funcInput):
    funcInput.config(state=tk.NORMAL)
    funcInput.delete("1.0", tk.END)
    funcInput.config(state=tk.DISABLED)

def drawChart(fig, canvas, x, y):
    fig.clear()
    fig.add_subplot().plot(x, y)
    plt.grid(axis="both", color='gray', linestyle='--', linewidth=0.5)
    canvas.draw_idle()

def inputEntry(textBox, command):
    textEntry = str(command)
    textBox.config(state=tk.NORMAL)
    textBox.insert(tk.END, textEntry)
    textBox.config(state=tk.DISABLED)

def numberInput(textBox, num):
    inputEntry(textBox, num)

def functionInput(textBox, function, frame):
    inputEntry(textBox, function)
    hideButtons(frame)

def addition(textBox, frame):
    inputEntry(textBox, "+")
    hideButtons(frame)

def subtraction(textBox, frame):
    inputEntry(textBox, "-")
    hideButtons(frame)

def multiplication(textBox, frame):
    inputEntry(textBox, "*")
    hideButtons(frame)

def division(textBox, frame):
    inputEntry(textBox, "/")
    hideButtons(frame)


def error_message():
    # Create a new top-level window for the error message
    error_window = tk.Toplevel()
    error_window.title("Error")

    # Set the size of the pop-up window
    error_window.geometry("250x100")

    # Label to display the error message
    label = tk.Label(error_window, text="Syntax Error", font=("Arial", 12))
    label.pack(pady=20)

    # Button to close the error message pop-up
    button = tk.Button(error_window, text="Close", command=error_window.destroy)
    button.pack()

def graphInput(funcInput, fig, canvas, x):
    inputString = funcInput.get("1.0", tk.END)
    try:
        y = np.full_like(x, eval(inputString))
        drawChart(fig, canvas, x, y)
        deleteText(funcInput)
    except SyntaxError:
        error_message()
        deleteText(funcInput)

def main():
    # Window set up
    window = tk.Tk()
    window.title("Differential Equation Visualizer and Solver")
    window.geometry("550x800")
    window.resizable(width=False, height=False)
    #window.eval("tk::PlaceWindow . center")

    # x and y
    x = np.linspace(-10, 10, 10000)
    y = np.full_like(x, np.nan)

    # Graph initialization
    fig, ax = plt.subplots()
    plt.grid(axis="both", color='gray', linestyle='--', linewidth=0.5)
    ax.plot(x, y)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()

    # Text box
    frm_txt = tk.Frame(master=window)
    equationText = tk.Text(master=frm_txt,height=1, width=30, bg="white", fg="black")
    #button for graph
    equationButton = tk.Button(master=frm_txt, text="Graph", command=lambda: graphInput(equationText, fig, canvas, x))
    equationText.grid(row=0, column=0, sticky="e")
    equationButton.grid(row=0, column=1, sticky="w")


    #add flag var so no overlap
    # Operation buttons
    frm_operations = tk.Frame(master=window)
    additionButton = tk.Button(master=frm_operations, text="+", command=lambda: addition(equationText, frm_operations))
    additionButton.grid(row=0, column=0, sticky="w")
    subtractionButton = tk.Button(master=frm_operations, text="-", command=lambda: subtraction(equationText, frm_operations))
    subtractionButton.grid(row=0, column=1, sticky="e")
    multiplicationButton = tk.Button(master=frm_operations, text="*", command=lambda: multiplication(equationText, frm_operations))
    multiplicationButton.grid(row=1, column=0, sticky="w")
    divisionButton = tk.Button(master=frm_operations, text="/", command=lambda: division(equationText, frm_operations))
    divisionButton.grid(row=1, column=1, sticky="e")

    # Function buttons
    frm_functions = tk.Frame(master=window)
    print("hit the button")
    xButton = tk.Button(master=frm_functions, text="x", command=lambda: functionInput(equationText, "x", frm_functions))
    xButton.grid(row=0, column=0)
    LPButton = tk.Button(master=frm_functions, text="(", command=lambda: functionInput(equationText, "(", frm_functions))
    LPButton.grid(row=0, column=1)
    RPButton = tk.Button(master=frm_functions, text=")", command=lambda: functionInput(equationText, ")", frm_functions))
    RPButton.grid(row=0, column=2)
    cosineButton = tk.Button(master=frm_functions, text="cos()", command=lambda: functionInput(equationText, "np.cos(", frm_functions))
    cosineButton.grid(row=1, column=0)

    # Buttons
    frm_button = tk.Frame(master=window)
    oneButton = tk.Button(master=frm_button, text="1", command=lambda: numberInput(equationText, 1))
    twoButton = tk.Button(master=frm_button, text="2", command=lambda: numberInput(equationText, 2))
    threeButton = tk.Button(master=frm_button, text="3", command=lambda: numberInput(equationText, 3))
    fourButton = tk.Button(master=frm_button, text="4", command=lambda: numberInput(equationText, 4))
    fiveButton = tk.Button(master=frm_button, text="5", command=lambda: numberInput(equationText, 5))
    sixButton = tk.Button(master=frm_button, text="6", command=lambda: numberInput(equationText, 6))
    sevenButton = tk.Button(master=frm_button, text="7", command=lambda: numberInput(equationText, 7))
    eightButton = tk.Button(master=frm_button, text="8", command=lambda: numberInput(equationText, 8))
    nineButton = tk.Button(master=frm_button, text="9", command=lambda: numberInput(equationText, 9))
    zeroButton = tk.Button(master=frm_button, text="0", command=lambda: numberInput(equationText, 0))
    operationButton = tk.Button(master=frm_button, text="Operations", command=lambda: showButtons(frm_operations))
    functionButton = tk.Button(master=frm_button, text="Functions", command=lambda: showButtons(frm_functions))

    oneButton.grid(row=0, column=0)
    twoButton.grid(row=0, column=1)
    threeButton.grid(row=0, column=2)
    zeroButton.grid(row=0, column=3, sticky="w")
    fourButton.grid(row=1, column=0)
    fiveButton.grid(row=1, column=1)
    sixButton.grid(row=1, column=2)
    operationButton.grid(row=1, column=3, sticky="w")
    sevenButton.grid(row=2, column=0)
    eightButton.grid(row=2, column=1)
    nineButton.grid(row=2, column=2)
    functionButton.grid(row=2, column=3, sticky="w")

    # Reset text
    resetButton = tk.Button(master=window, text="Reset", command=lambda: deleteText(equationText))

    # Close window
    windowClose = tk.Button(master=window, text="Close Application", command=window.destroy)

    # Widgets placement
    canvas_widget.grid(row=0, column=0, padx=10, pady=10)
    frm_txt.grid(row=1, column=0)
    frm_button.grid(row=2, column=0)
    resetButton.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    windowClose.grid(row=3, column=0, padx=10, pady=10, sticky="e")

    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    window.rowconfigure(1, weight=0)

    window.rowconfigure(2, weight=1)

    window.rowconfigure(3, weight=0)

    # Window main loop
    window.mainloop()

if __name__ == "__main__":
    main()