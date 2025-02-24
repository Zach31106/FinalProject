import tkinter as tk

window = tk.Tk()
window2 = tk.Tk()
window.title('Main Window')
window.geometry('400x600')
window2.title('Other Window')
window2.geometry('400x600')
button = tk.Button(window, text='Stop', width=25, command=window2.destroy)
button.pack()
window.mainloop()