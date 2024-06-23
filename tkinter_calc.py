import tkinter as tk
from PIL import Image, ImageTk

# Function to update the display when buttons are clicked
def button_click(symbol):
    current = display_var.get()
    if current == "0" and symbol != ".":
        display_var.set(symbol)
    else:
        display_var.set(current + symbol)

# Function to evaluate the expression and update the display
def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except Exception as e:
        display_var.set("Error")

# Function to clear the display
def clear():
    display_var.set("0")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Set fixed window size
root.geometry("340x535")  # Width x Height

# Disable resizing of the window
root.resizable(False, False)

root.iconbitmap('download.ico')
root.wm_iconbitmap('download.ico')
root.iconphoto(False, 'download.ico')

# Variable to hold the current display value
display_var = tk.StringVar()
display_var.set("0")

# Entry widget to display the result
display = tk.Entry(root, textvariable=display_var, font=('Arial', 20), bd=10, insertwidth=4, width=14, justify='right')
display.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, column) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=('Arial', 18), padx=20, pady=20,
                           command=calculate)
    elif text == 'C':
        button = tk.Button(root, text=text, font=('Arial', 18), padx=20, pady=20,
                           command=clear)
    else:
        button = tk.Button(root, text=text, font=('Arial', 18), padx=20, pady=20,
                           command=lambda symbol=text: button_click(symbol))
    button.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')

# Binding the Enter key to calculate function
root.bind('<Return>', lambda event: calculate())

# Binding the Backspace key to clear function
root.bind('<BackSpace>', lambda event: clear())

# Run the main loop
root.mainloop()
