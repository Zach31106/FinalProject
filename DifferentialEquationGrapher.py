import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from sympy import symbols, Eq, solve, lambdify
from sympy.parsing.sympy_parser import parse_expr
from scipy.integrate import odeint


class GraphPlane:
    window = tk.Tk()
    fig, ax = plt.subplots()
    frm_graph = tk.Frame(window)
    canvas = FigureCanvasTkAgg(fig, master=frm_graph)

    x = np.linspace(-10, 10, 10000)
    y = np.full_like(x, np.nan)
    IVP1 = 0
    IVP2 = 0
    input_stack = []

    def __init__(self, name, size, color, mode):
        self.name = name
        self.size = size
        self.color = color
        self.mode = mode

    @staticmethod
    def showButtons(frame):  # Function that shows groups of buttons
        frame.grid(row=2, column=0)
        frame.update_idletasks()

    @staticmethod
    def hideButtons(frame):  # Function that hides groups of buttons
        frame.grid_remove()

    @staticmethod
    def deleteText(funcInput):  # Function that clears a text box
        funcInput.config(state=tk.NORMAL)
        funcInput.delete("1.0", tk.END)
        funcInput.config(state=tk.DISABLED)

    @classmethod
    def setValue(cls, value, funcInput):  # Function that sets initial conditions
        try:
            if value == "IVP1":
                cls.IVP1 = int(funcInput.get("1.0", tk.END))
                cls.deleteText(funcInput)
                funcInput.config(state=tk.NORMAL)
            if value == "IVP2":
                cls.IVP2 = int(funcInput.get("1.0", tk.END))
                cls.deleteText(funcInput)
                funcInput.config(state=tk.NORMAL)
        except ValueError:
            return

    @staticmethod
    def step_function(x):  # Function that represents the step function
        return np.where(x >= 0, 1, 0)

    def impulse_function(self, a):  # Function that gives an estimate for the dirac-delta function
        return (5 * self.step_function(a + 0.1)) - (5 * self.step_function(a - 0.1))

    @classmethod
    def inputEntry(cls, textBox1, function1, textBox2, function2):  # Function that types an input into a textbox
        textEntry1 = str(function1)
        textBox1.config(state=tk.NORMAL)
        textBox1.insert(tk.END, textEntry1)
        textBox1.config(state=tk.DISABLED)

        textEntry2 = str(function2)
        textBox2.config(state=tk.NORMAL)
        textBox2.insert(tk.END, textEntry2)
        textBox2.config(state=tk.DISABLED)

        cls.input_stack.append((textEntry1, textEntry2))

    @classmethod
    def deleteLastInput(cls, textBox1, textBox2):  # Function that deletes the last inputted item
        if not cls.input_stack:
            return

        last_entry1, last_entry2 = cls.input_stack.pop()

        textBox1.config(state=tk.NORMAL)
        current1 = textBox1.get("1.0", tk.END)
        textBox1.delete("1.0", tk.END)
        textBox1.insert("1.0", current1.rstrip().rsplit(last_entry1, 1)[0])
        textBox1.config(state=tk.DISABLED)

        textBox2.config(state=tk.NORMAL)
        current2 = textBox2.get("1.0", tk.END)
        textBox2.delete("1.0", tk.END)
        textBox2.insert("1.0", current2.rstrip().rsplit(last_entry2, 1)[0])
        textBox2.config(state=tk.DISABLED)

    @classmethod
    def functionInput(cls, textBox1, function1, textBox2, function2,
                      frame):  # Function that types a computational function into a textbox
        cls.inputEntry(textBox1, function1, textBox2, function2)
        cls.hideButtons(frame)

    @staticmethod
    def errorMessage():  # Function that handles input errors
        error_window = tk.Toplevel()
        error_window.title("Error")
        error_window.geometry("250x100")
        label = tk.Label(error_window, text="Syntax Error", font=("Arial", 12))
        label.pack(pady=20)
        button = tk.Button(error_window, text="Close", command=error_window.destroy)
        button.pack()

    @staticmethod
    def instructions():  # Functions that displays instructions
        instructions_window = tk.Tk()
        instructions_window.title("Instructions")
        instructions_window.resizable(width=False, height=False)
        # instructions_window.eval("tk::PlaceWindow . center")
        label = tk.Label(instructions_window,
                         text="This is a graphing calculator that allows for differential equations. For a normal equation, press the buttons that correspond to your equation then enter graph.\n Functions like sine and the natural logarithm can be found through the functions button. For differential equations, first type in your initial values and hit their corresponding button.\n Next, set the range for solving. The left most bound will be where your initial conditions are set. Now you can enter your equation, hit graph, and see the solution.",
                         font=("Arial", 12))
        label.pack(pady=20)
        button = tk.Button(instructions_window, text="Close", command=instructions_window.destroy)
        button.pack()

    @staticmethod
    def slope_field(f, x_range, y_range, step=0.2):  # Function that solves a slope field
        x, y = np.meshgrid(np.arange(x_range[0], x_range[1], step),
                           np.arange(y_range[0], y_range[1], step))
        u = np.ones_like(x)
        v = f(x, y)
        norm = np.sqrt(u ** 2 + v ** 2)
        return x, y, u / norm, v / norm

    @classmethod
    def plot_slope_field(cls, f, x_range, y_range, ax):  # Function that plots a slope field
        x, y, u, v = cls.slope_field(f, x_range, y_range)
        ax.quiver(x, y, u, v, color='blue')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Slope Field')
        ax.set_xlim(x_range)
        ax.set_ylim(y_range)
        ax.grid(True)

    @classmethod
    def drawChart(cls, fig, canvas, x, y, XL, XR, slope):  # Function that draws the graph
        fig.clear()
        x_range = (XL, XR)
        ax = fig.add_subplot()
        ax.plot(x, y, color='black')
        if slope:
            cls.plot_slope_field(slope, x_range, ax.get_ylim(), ax)
        ax.set_xlim(x_range)
        ax.grid(axis="both", color='gray', linestyle='--', linewidth=0.5)
        ax.axvline(x=0, color='black', linewidth=1)
        ax.axhline(y=0, color='black', linewidth=1)

        canvas.draw_idle()

    @classmethod
    def graphInput(cls, funcInput1, funcInput2, funcInput3, funcInput4, fig, canvas,
                   x):  # Function that graphs an inputted equation with error handling
        input_value = funcInput3.get("1.0", tk.END).strip()
        if input_value:
            XL = float(input_value)
        else:
            XL = 0
        input_value_2 = funcInput4.get("1.0", tk.END).strip()
        if input_value_2:
            XR = float(input_value_2)
        else:
            XR = 1
        inputString = funcInput2.get("1.0", tk.END)
        try:
            if "y2" in inputString:
                title = str(funcInput1.get("1.0", tk.END))
                plt.title(title)
                inputString = inputString.replace("np.", "")
                lhs = parse_expr(inputString.split("=", 1)[0])
                rhs = parse_expr(inputString.split("=", 1)[1])
                # Define symbolic variables
                x, y2, y1, y0 = symbols('x y2 y1 y0')

                # Define the differential equation
                differential_equation = Eq(lhs, rhs)

                # Solve for y'' (y2)
                y2 = solve(differential_equation, y2)[0]  # Extract y''

                # Convert the symbolic solution into a numerical function
                y2_function = lambdify((x, y0, y1), y2, modules=['numpy', {'step_function': cls.step_function},
                                                                 {'impulse_function': cls.impulse_function}])

                # Initial conditions: [y(0), y'(0)]
                init_conditions = [cls.IVP1, cls.IVP2]

                # Time points
                time = np.linspace(XL, XR, 1001)

                # Define the system of ODEs using the solved equation
                def system_of_odes(y, t):
                    y0, y1 = y  # y1 = y, y2 = y'
                    x = t
                    y2 = y2_function(x, y0, y1)
                    return y1, y2

                # Solve the ODE numerically
                solution = odeint(system_of_odes, init_conditions, time)
                cls.drawChart(fig, canvas, time, solution[:, 0], XL, XR, None)
                title = funcInput1.get("1.0", tk.END).replace("*", "")
                plt.title(title + "y(" + str(XL) + ") = " + str(cls.IVP1) + ", y'(" + str(XL) + ") = " + str(cls.IVP2))
                cls.deleteText(funcInput1)
                cls.deleteText(funcInput2)
            elif "y1" in inputString:
                inputString = inputString.replace("np.", "")
                lhs = parse_expr(inputString.split("=", 1)[0])
                rhs = parse_expr(inputString.split("=", 1)[1])
                x, y1, y0 = symbols('x, y1 y0')
                differential_equation = Eq(lhs, rhs)
                y1 = solve(differential_equation, y1)[0]
                y1_function = lambdify((x, y0), y1, modules=['numpy', {'step_function': cls.step_function},
                                                             {'impulse_function': cls.impulse_function}])
                init_condition = cls.IVP1
                time = np.linspace(XL, XR, 1001)

                def system_of_odes(y, t):
                    y0 = y
                    x = t
                    y1 = y1_function(x, y0)
                    return y1

                solution = odeint(system_of_odes, init_condition, time)
                cls.drawChart(fig, canvas, time, solution[:], XL, XR, y1_function)
                title = funcInput1.get("1.0", tk.END).replace("*", "")
                plt.title(title + "y(" + str(XL) + ") = " + str(cls.IVP1))
                cls.deleteText(funcInput1)
                cls.deleteText(funcInput2)
            elif "y0=" in inputString:
                inputString = inputString.split("=", 1)[1]
                x = np.linspace(XL, XR, 1001)
                y = np.full_like(x, eval(inputString))
                cls.drawChart(fig, canvas, x, y, XL, XR, None)
                title = funcInput1.get("1.0", tk.END).replace("*", "")
                plt.title(title)
                cls.deleteText(funcInput1)
                cls.deleteText(funcInput2)
            else:
                x = np.linspace(XL, XR, 1001)
                y = np.full_like(x, eval(inputString))
                cls.drawChart(fig, canvas, x, y, XL, XR, None)
                title = funcInput1.get("1.0", tk.END).replace("*", "")
                plt.title(title)
                cls.deleteText(funcInput1)
                cls.deleteText(funcInput2)

        except SyntaxError:
            cls.errorMessage()
            cls.deleteText(funcInput1)
            cls.deleteText(funcInput2)

    def windowCreate(self):
        self.window.title(self.name)
        self.window.geometry(f"{self.size[0]}x{self.size[1]}")
        self.window.configure(background=self.color)
        self.window.resizable(width=False, height=False)
        #self.window.eval("tk::PlaceWindow . center")
        return self.window

    def graphInitialization(self):
        plt.grid(axis="both", color='gray', linestyle='--', linewidth=0.5)
        self.ax.plot(self.x, self.y)
        self.ax.axvline(x=0, color='black', linewidth=1)
        self.ax.axhline(y=0, color='black', linewidth=1)
        canvas_widget = self.canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(self.canvas, self.frm_graph)
        toolbar.children['!button4'].pack_forget()
        toolbar.update()
        self.frm_graph.grid(row=1, column=0, padx=10, pady=10)


    def widgetsCreationAndPlacement(self):
        # Instructions
        instructionsButton = tk.Button(self.window, text="Differential Equation Visualizer", command=self.instructions)

        # Text box
        frm_txt = tk.Frame(master=self.window)
        equationText = tk.Text(master=frm_txt, wrap="word", height=1, width=30, bg="white", fg="black")
        equationText.config(state=tk.DISABLED)
        equationText.grid(row=0, column=0, columnspan=3)

        calculationText = tk.Text(master=frm_txt, wrap="word")
        equationText.config(state=tk.DISABLED)

        spanXL = tk.Text(master=frm_txt, height=1, width=5, bg="white", fg="black")
        spanXR = tk.Text(master=frm_txt, height=1, width=5, bg="white", fg="black")
        spanLabel = tk.Label(master=frm_txt, text="<= x <=", height=1, width=5)

        spanXL.grid(row=1, column=0)
        spanLabel.grid(row=1, column=1)
        spanXR.grid(row=1, column=2)
        # Button frame initializations
        frm_Buttons = tk.Frame(master=self.window)

        # Left buttons, inputEntry(typedText, typedFunction, equationText, equationFunction,
        frm_LButton = tk.Frame(master=frm_Buttons)
        xButton = tk.Button(master=frm_LButton, text="x",
                            command=lambda: self.inputEntry(equationText, "x", calculationText, "x"), width=2)
        y1Button = tk.Button(master=frm_LButton, text="y'",
                             command=lambda: self.inputEntry(equationText, "y'", calculationText, "y1"), width=2)
        y2Button = tk.Button(master=frm_LButton, text="y''",
                             command=lambda: self.inputEntry(equationText, "y''", calculationText, "y2"), width=2)
        LPButton = tk.Button(master=frm_LButton, text="(",
                             command=lambda: self.inputEntry(equationText, "(", calculationText, "("), width=2)
        RPButton = tk.Button(master=frm_LButton, text=")",
                             command=lambda: self.inputEntry(equationText, ")", calculationText, ")"), width=2)
        yButton = tk.Button(master=frm_LButton, text="y",
                            command=lambda: self.inputEntry(equationText, "y", calculationText, "y0"), width=2)
        exponentButton = tk.Button(master=frm_LButton, text="^a",
                                   command=lambda: self.inputEntry(equationText, "^(", calculationText, "**("), width=2)
        squareButton = tk.Button(master=frm_LButton, text="^2",
                                 command=lambda: self.inputEntry(equationText, "^2", calculationText, "**2"), width=2)
        absoluteButton = tk.Button(master=frm_LButton, text="||",
                                   command=lambda: self.inputEntry(equationText, "abs(", calculationText, "abs("), width=2)
        sqrtButton = tk.Button(master=frm_LButton, text="√",
                               command=lambda: self.inputEntry(equationText, "√(", calculationText, "np.sqrt("), width=2)
        piButton = tk.Button(master=frm_LButton, text="π",
                             command=lambda: self.inputEntry(equationText, "π", calculationText, "np.pi"), width=2)
        eButton = tk.Button(master=frm_LButton, text="e",
                            command=lambda: self.inputEntry(equationText, "e", calculationText, "np.exp(1)"), width=2)

        IVP1Text = tk.Text(master=frm_LButton, height=1, width=5, bg="white", fg="black")
        IVP2Text = tk.Text(master=frm_LButton, height=1, width=5, bg="white", fg="black")
        IVP1Button = tk.Button(master=frm_LButton, text="y(x1)", command=lambda: self.setValue("IVP1", IVP1Text), width=2)
        IVP2Button = tk.Button(master=frm_LButton, text="y'(x1)", command=lambda: self.setValue("IVP2", IVP2Text), width=2)

        xButton.grid(row=0, column=0, sticky="w")
        yButton.grid(row=0, column=1, sticky="w")
        y1Button.grid(row=0, column=2, sticky="w")
        y2Button.grid(row=0, column=3, sticky="w")

        squareButton.grid(row=1, column=0, sticky="w")
        exponentButton.grid(row=1, column=1, sticky="w")
        LPButton.grid(row=1, column=2, sticky="w")
        RPButton.grid(row=1, column=3, sticky="w")

        absoluteButton.grid(row=2, column=0, sticky="w")
        sqrtButton.grid(row=2, column=1, sticky="w")
        piButton.grid(row=2, column=2, sticky="w")
        eButton.grid(row=2, column=3, sticky="w")

        IVP1Button.grid(row=3, column=0)
        IVP1Text.grid(row=3, column=1)
        IVP2Button.grid(row=3, column=2)
        IVP2Text.grid(row=3, column=3)

        # Middle buttons
        frm_MButton = tk.Frame(master=frm_Buttons)
        oneButton = tk.Button(master=frm_MButton, text="1",
                              command=lambda: self.inputEntry(equationText, 1, calculationText, 1))
        twoButton = tk.Button(master=frm_MButton, text="2",
                              command=lambda: self.inputEntry(equationText, 2, calculationText, 2))
        threeButton = tk.Button(master=frm_MButton, text="3",
                                command=lambda: self.inputEntry(equationText, 3, calculationText, 3))
        fourButton = tk.Button(master=frm_MButton, text="4",
                               command=lambda: self.inputEntry(equationText, 4, calculationText, 4))
        fiveButton = tk.Button(master=frm_MButton, text="5",
                               command=lambda: self.inputEntry(equationText, 5, calculationText, 5))
        sixButton = tk.Button(master=frm_MButton, text="6",
                              command=lambda: self.inputEntry(equationText, 6, calculationText, 6))
        sevenButton = tk.Button(master=frm_MButton, text="7",
                                command=lambda: self.inputEntry(equationText, 7, calculationText, 7))
        eightButton = tk.Button(master=frm_MButton, text="8",
                                command=lambda: self.inputEntry(equationText, 8, calculationText, 8))
        nineButton = tk.Button(master=frm_MButton, text="9",
                               command=lambda: self.inputEntry(equationText, 9, calculationText, 9))
        zeroButton = tk.Button(master=frm_MButton, text="0",
                               command=lambda: self.inputEntry(equationText, 0, calculationText, 0))
        additionButton = tk.Button(master=frm_MButton, text="+",
                                   command=lambda: self.inputEntry(equationText, "+", calculationText, "+"))
        subtractionButton = tk.Button(master=frm_MButton, text="-",
                                      command=lambda: self.inputEntry(equationText, "-", calculationText, "-"))
        multiplicationButton = tk.Button(master=frm_MButton, text="*",
                                         command=lambda: self.inputEntry(equationText, "*", calculationText, "*"))
        divisionButton = tk.Button(master=frm_MButton, text="/",
                                   command=lambda: self.inputEntry(equationText, "/", calculationText, "/"))
        decimalButton = tk.Button(master=frm_MButton, text=".",
                                  command=lambda: self.inputEntry(equationText, ".", calculationText, "."))
        equalButton = tk.Button(master=frm_MButton, text="=",
                                command=lambda: self.inputEntry(equationText, "=", calculationText, "="))

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

        functionButton = tk.Button(master=frm_RButton, text="Functions", command=lambda: self.showButtons(frm_functions),
                                   width=10)
        frm_functions = tk.Frame(master=self.window)
        cosineButton = tk.Button(master=frm_functions, text="cos()",
                                 command=lambda: self.functionInput(equationText, "cos(", calculationText, "np.cos(",
                                                               frm_functions))
        sineButton = tk.Button(master=frm_functions, text="sin()",
                               command=lambda: self.functionInput(equationText, "sin(", calculationText, "np.sin(",
                                                             frm_functions))
        tangentButton = tk.Button(master=frm_functions, text="tan()",
                                  command=lambda: self.functionInput(equationText, "tan(", calculationText, "np.tan(",
                                                                frm_functions))
        arcsinButton = tk.Button(master=frm_functions, text="arcsin()",
                                 command=lambda: self.functionInput(equationText, "arcsin(", calculationText, "np.arcsin(",
                                                               frm_functions))
        arccosButton = tk.Button(master=frm_functions, text="arccos()",
                                 command=lambda: self.functionInput(equationText, "arccos(", calculationText, "np.arccos(",
                                                               frm_functions))
        arctanButton = tk.Button(master=frm_functions, text="arctan()",
                                 command=lambda: self.functionInput(equationText, "arctan(", calculationText, "np.arctan(",
                                                               frm_functions))
        lnButton = tk.Button(master=frm_functions, text="ln()",
                             command=lambda: self.functionInput(equationText, "ln(", calculationText, "np.log(",
                                                           frm_functions))
        stepButton = tk.Button(master=frm_functions, text="u(x-a)",
                               command=lambda: self.functionInput(equationText, "u(", calculationText, "step_function(",
                                                             frm_functions))
        impulseButton = tk.Button(master=frm_functions, text="δ(x-a)",
                                  command=lambda: self.functionInput(equationText, "δ(", calculationText,
                                                                "impulse_function(",
                                                                frm_functions))
        exitButton = tk.Button(master=frm_functions, text="Exit", command=lambda: self.hideButtons(frm_functions))

        sineButton.grid(row=0, column=0)
        cosineButton.grid(row=0, column=1)
        tangentButton.grid(row=0, column=2)

        arcsinButton.grid(row=1, column=0)
        arccosButton.grid(row=1, column=1)
        arctanButton.grid(row=1, column=2)

        lnButton.grid(row=2, column=0)
        stepButton.grid(row=2, column=1)
        impulseButton.grid(row=2, column=2)

        exitButton.grid(row=3, column=2, sticky="e")

        deleteButton = tk.Button(master=frm_RButton, text="Delete",
                                 command=lambda: self.deleteLastInput(equationText, calculationText), width=5)
        equationButton = tk.Button(master=frm_RButton, text="Graph",
                                   command=lambda: self.graphInput(equationText, calculationText, spanXL, spanXR, self.fig,
                                                              self.canvas,
                                                              self.x),
                                   width=10)

        functionButton.grid(row=0, column=0, columnspan=4, sticky="e")
        deleteButton.grid(row=1, column=2, columnspan=2)
        equationButton.grid(row=2, column=0, columnspan=4, sticky="e")

        # Frame Placements
        frm_LButton.grid(row=0, column=0)
        frm_MButton.grid(row=0, column=1)
        frm_RButton.grid(row=0, column=2)

        # Reset text
        resetButton = tk.Button(master=self.window, text="Reset",
                                command=lambda: (self.deleteText(equationText), self.deleteText(calculationText)))

        # Close window
        windowClose = tk.Button(master=self.window, text="Close Application", command=self.window.destroy)

        instructionsButton.grid(row=0, column=0)
        self.frm_graph.grid(row=1, column=0, padx=10, pady=10)
        frm_txt.grid(row=2, column=0)
        frm_Buttons.grid(row=3, column=0)
        resetButton.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        windowClose.grid(row=4, column=0, padx=10, pady=10, sticky="e")

    def rowColumnSetup(self):
        self.window.rowconfigure(0, weight=0)
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=0)
        self.window.rowconfigure(2, weight=0)
        self.window.rowconfigure(3, weight=0)
        self.window.rowconfigure(4, weight=0)

    def runProgram(self):
        runWindow = self.windowCreate()
        runWindow.mainloop()

def main():
    window = GraphPlane("Calculator", (550, 800), "#333333", "diffEq")
    window.graphInitialization()
    window.widgetsCreationAndPlacement()
    window.rowColumnSetup()
    window.runProgram()

if __name__ == "__main__":
    main()
