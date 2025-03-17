import numpy as np


cosineButton = tk.Button(master=frm_functions, text="cos()", command=lambda: functionInput(equationText, "np.cos(", frm_functions))
cosineButton.grid(row=1, column=0)
sineButton = tk.Button(master=frm_functions, text="sin()", command=lambda: functionInput(equationText, "np.sin(", frm_functions))
sineButton.grid(row=1, column=1)
tangentButton = tk.Button(master=frm_functions, text="tan()", command=lambda: functionInput(equationText, "np.tan(", frm_functions))
tangentButton.grid(row=1, column=2)
