import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
#import sympy as sp

start_x = 0
start_y = 0
ax = None
canvas = None

# Function to handle mouse button press
def on_press(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y

# Function to handle mouse movement
def on_move(event):
    global start_x, start_y, ax, canvas
    if ax is None or canvas is None:
        return  # Ensure ax and canvas are defined before proceeding

    dx = event.x - start_x
    dy = event.y - start_y

    ax.set_xlim([ax.get_xlim()[0] - dx/10, ax.get_xlim()[1] - dx/10])
    ax.set_ylim([ax.get_ylim()[0] + dy/10, ax.get_ylim()[1] + dy/10])

    canvas.draw_idle()

    start_x = event.x
    start_y = event.y

def showButtons(frame):  # Function that shows groups of buttons
    frame.grid(row=1, column=0)
    frame.update_idletasks()


def hideButtons(frame):  # Function that hides groups of buttons
    frame.grid_remove()


def deleteText(funcInput):  # Function that clears a text box
    funcInput.config(state=tk.NORMAL)
    funcInput.delete("1.0", tk.END)
    funcInput.config(state=tk.DISABLED)


def drawChart(fig, canvas_widget, x, y):  # Function that redraws a graph
    global ax, canvas  # Ensure we're modifying the global ax

    fig.clear()
    ax = fig.add_subplot()  # Reassign ax properly
    ax.plot(x, y)
    ax.grid(axis="both", color='gray', linestyle='--', linewidth=0.5)

    canvas.draw_idle()

    canvas_widget.bind("<ButtonPress-1>", on_press)
    canvas_widget.bind("<B1-Motion>", on_move)


def inputEntry(textBox, function):  # Function that types an input into a textbox
    textEntry = str(function)
    textBox.config(state=tk.NORMAL)
    textBox.insert(tk.END, textEntry)
    textBox.config(state=tk.DISABLED)


def functionInput(textBox, function, frame):  # Function that types a computational function into a textbox
    inputEntry(textBox, function)
    hideButtons(frame)


def errorMessage():  # Function that handles input errors
    error_window = tk.Toplevel()
    error_window.title("Error")
    error_window.geometry("250x100")
    label = tk.Label(error_window, text="Syntax Error", font=("Arial", 12))
    label.pack(pady=20)
    button = tk.Button(error_window, text="Close", command=error_window.destroy)
    button.pack()


def graphInput(funcInput, fig, canvas_widget, x):  # Function that graphs an inputted equation with error handling
    inputString = funcInput.get("1.0", tk.END)
    try:
        y = np.full_like(x+2, eval(inputString))
        drawChart(fig, canvas_widget, x, y)
        deleteText(funcInput)

    except SyntaxError:
        errorMessage()
        deleteText(funcInput)


def main():
    global ax, canvas, start_x, start_y

    # Window set up
    window = tk.Tk()
    window.title("Differential Equation Visualizer and Solver")
    window.geometry("550x800")
    window.resizable(width=False, height=False)
    window.eval("tk::PlaceWindow . center")

    # x and y
    x = np.linspace(-10, 10, 10000)
    y = np.full_like(x, np.nan)

    # Graph initialization
    fig, ax = plt.subplots()
    plt.grid(axis="both", color='gray', linestyle='--', linewidth=0.5)
    ax.plot(x, y)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.bind("<ButtonPress-1>", on_press)
    canvas_widget.bind("<B1-Motion>", on_move)

    # Text box
    frm_txt = tk.Frame(master=window)
    equationText = tk.Text(master=frm_txt, height=1, width=30, bg="white", fg="black")
    equationText.config(state=tk.DISABLED)
    equationText.grid(row=0, column=0)

    # Button frame initializations
    frm_Buttons = tk.Frame(master=window)

    # Left buttons
    frm_LButton = tk.Frame(master=frm_Buttons)
    xButton = tk.Button(master=frm_LButton, text="x", command=lambda: inputEntry(equationText, "x"), width=2)
    dyButton = tk.Button(master=frm_LButton, text="dy", command=lambda: inputEntry(equationText, "dy"), width=2)
    dxButton = tk.Button(master=frm_LButton, text="dx", command=lambda: inputEntry(equationText, "dx"), width=2)
    LPButton = tk.Button(master=frm_LButton, text="(", command=lambda: inputEntry(equationText, "("), width=2)
    RPButton = tk.Button(master=frm_LButton, text=")", command=lambda: inputEntry(equationText, ")"), width=2)
    yButton = tk.Button(master=frm_LButton, text="y", command=lambda: inputEntry(equationText, "y"), width=2)
    exponentButton = tk.Button(master=frm_LButton, text="^a", command=lambda: inputEntry(equationText, "**("), width=2)
    squareButton = tk.Button(master=frm_LButton, text="^2", command=lambda: inputEntry(equationText, "**2"), width=2)
    absoluteButton = tk.Button(master=frm_LButton, text="||", command=lambda: inputEntry(equationText, "abs("), width=2)
    sqrtButton = tk.Button(master=frm_LButton, text="√", command=lambda: inputEntry(equationText, "np.sqrt("), width=2)
    piButton = tk.Button(master=frm_LButton, text="π", command=lambda: inputEntry(equationText, "np.pi"), width=2)
    eButton = tk.Button(master=frm_LButton, text="e", command=lambda: inputEntry(equationText, "np.e"), width=2)
    IVP1Button = tk.Button(master=frm_LButton, text="y(0)", command=lambda: None)
    IVP2Button = tk.Button(master=frm_LButton, text="y'(0)", command=lambda: None)

    xButton.grid(row=0, column=0, sticky="w")
    yButton.grid(row=0, column=1, sticky="w")
    dxButton.grid(row=0, column=2, sticky="w")
    dyButton.grid(row=0, column=3, sticky="w")

    squareButton.grid(row=1, column=0, sticky="w")
    exponentButton.grid(row=1, column=1, sticky="w")
    LPButton.grid(row=1, column=2, sticky="w")
    RPButton.grid(row=1, column=3, sticky="w")

    absoluteButton.grid(row=2, column=0, sticky="w")
    sqrtButton.grid(row=2, column=1, sticky="w")
    piButton.grid(row=2, column=2, sticky="w")
    eButton.grid(row=2, column=3, sticky="w")

    IVP1Button.grid(row=3, column=0, columnspan=2)
    IVP2Button.grid(row=3, column=2, columnspan=2)

    # Middle buttons
    frm_MButton = tk.Frame(master=frm_Buttons)
    oneButton = tk.Button(master=frm_MButton, text="1", command=lambda: inputEntry(equationText, 1))
    twoButton = tk.Button(master=frm_MButton, text="2", command=lambda: inputEntry(equationText, 2))
    threeButton = tk.Button(master=frm_MButton, text="3", command=lambda: inputEntry(equationText, 3))
    fourButton = tk.Button(master=frm_MButton, text="4", command=lambda: inputEntry(equationText, 4))
    fiveButton = tk.Button(master=frm_MButton, text="5", command=lambda: inputEntry(equationText, 5))
    sixButton = tk.Button(master=frm_MButton, text="6", command=lambda: inputEntry(equationText, 6))
    sevenButton = tk.Button(master=frm_MButton, text="7", command=lambda: inputEntry(equationText, 7))
    eightButton = tk.Button(master=frm_MButton, text="8", command=lambda: inputEntry(equationText, 8))
    nineButton = tk.Button(master=frm_MButton, text="9", command=lambda: inputEntry(equationText, 9))
    zeroButton = tk.Button(master=frm_MButton, text="0", command=lambda: inputEntry(equationText, 0))
    additionButton = tk.Button(master=frm_MButton, text="+", command=lambda: inputEntry(equationText, "+"))
    subtractionButton = tk.Button(master=frm_MButton, text="-", command=lambda: inputEntry(equationText, "-"))
    multiplicationButton = tk.Button(master=frm_MButton, text="*", command=lambda: inputEntry(equationText, "*"))
    divisionButton = tk.Button(master=frm_MButton, text="/", command=lambda: inputEntry(equationText, "/"))
    decimalButton = tk.Button(master=frm_MButton, text=".", command=lambda: inputEntry(equationText, "."))
    equalButton = tk.Button(master=frm_MButton, text="=", command=lambda: inputEntry(equationText, "="))

    sevenButton.grid(row=0, column=0)
    eightButton.grid(row=0, column=1)
    nineButton.grid(row=0, column=2)
    divisionButton.grid(row=0, column=3)

    fourButton.grid(row=1, column=0)
    fiveButton.grid(row=1, column=1)
    sixButton.grid(row=1, column=2)
    multiplicationButton.grid(row=1, column=3)

    oneButton.grid(row=2, column=0)
    twoButton.grid(row=2, column=1)
    threeButton.grid(row=2, column=2)
    subtractionButton.grid(row=2, column=3)

    zeroButton.grid(row=3, column=0)
    decimalButton.grid(row=3, column=1)
    equalButton.grid(row=3, column=2)
    additionButton.grid(row=3, column=3)

    # Right Buttons
    frm_RButton = tk.Frame(master=frm_Buttons)

    functionButton = tk.Button(master=frm_RButton, text="Functions", command=lambda: showButtons(frm_functions), width=10)
    frm_functions = tk.Frame(master=window)
    cosineButton = tk.Button(master=frm_functions, text="cos()", command=lambda: functionInput(equationText, "np.cos(", frm_functions))
    sineButton = tk.Button(master=frm_functions, text="sin()", command=lambda: functionInput(equationText, "np.sin(", frm_functions))
    tangentButton = tk.Button(master=frm_functions, text="tan()", command=lambda: functionInput(equationText, "np.tan(", frm_functions))
    lnButton = tk.Button(master=frm_functions, text="ln()", command=lambda: functionInput(equationText, "np.log(", frm_functions))
    exitButton =tk.Button(master=frm_functions, text="Exit", command=lambda: hideButtons(frm_functions))

    sineButton.grid(row=0, column=0)
    cosineButton.grid(row=0, column=1)
    tangentButton.grid(row=0, column=2)

    lnButton.grid(row=1, column=0)

    exitButton.grid(row=2, column=2, sticky="e")

    leftButton = tk.Button(master=frm_RButton, text="<-", command=lambda: None)
    rightButton = tk.Button(master=frm_RButton, text="->", command=lambda: None)
    deleteButton = tk.Button(master=frm_RButton, text="Delete", command=lambda: None, width=5)
    equationButton = tk.Button(master=frm_RButton, text="Graph", command=lambda: graphInput(equationText, fig, canvas_widget, x), width=10)

    functionButton.grid(row=0, column=0, columnspan=4, sticky="e")
    leftButton.grid(row=1, column=0, columnspan=2, sticky="nsew")
    rightButton.grid(row=1, column=2, columnspan=2, sticky="nsew")
    deleteButton.grid(row=2, column=2, columnspan=2)
    equationButton.grid(row=3, column=0, columnspan=4, sticky="e")

    # Frame Placements
    frm_LButton.grid(row=0, column=0)
    frm_MButton.grid(row=0, column=1)
    frm_RButton.grid(row=0, column=2)

    # Reset text
    resetButton = tk.Button(master=window, text="Reset", command=lambda: deleteText(equationText))

    # Close window
    windowClose = tk.Button(master=window, text="Close Application", command=window.destroy)

    # Widgets placement
    canvas_widget.grid(row=0, column=0, padx=10, pady=10)
    frm_txt.grid(row=1, column=0)
    frm_Buttons.grid(row=2, column=0)
    resetButton.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    windowClose.grid(row=3, column=0, padx=10, pady=10, sticky="e")

    # Row and column configuration
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    window.rowconfigure(1, weight=0)

    window.rowconfigure(2, weight=1)

    window.rowconfigure(3, weight=0)

    # Window main loop
    window.mainloop()


if __name__ == "__main__":
    main()