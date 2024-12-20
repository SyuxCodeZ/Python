import tkinter as tk
from tkinter import ttk
import math

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_click(char):
    entry.insert(tk.END, char)

def clear():
    entry.delete(0, tk.END)

def delete():
    entry.delete(len(entry.get()) - 1)

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg='#282828')

# Center the window
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - width) // 2
y = (screen_height - height) // 2
root.geometry(f"{width}x{height}+{x}+{y}")

# Create the entry field
entry = tk.Entry(root, width=35, borderwidth=5, bg='#333333', fg='white')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the button pad
button_pad = ttk.Frame(root)
button_pad.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

button_text = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_index = 2
col_index = 0
for button_text in button_text:
    button = ttk.Button(button_pad, text=button_text, width=5, style='TButton')
    button.grid(row=row_index, column=col_index, padx=5, pady=5)
    button.bind('<Button-1>', lambda e, button=button: button_click(button['text']))
    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

# Create the scientific function pad
scientific_pad = ttk.Frame(root)
scientific_pad.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

scientific_buttons = [
    'sin', 'cos', 'tan', 'log',
    'ln', 'sqrt', 'pi', 'e',
    'x^y', 'x!', '(', ')'
]

row_index = 4
col_index = 0
for button_text in scientific_buttons:
    button = ttk.Button(scientific_pad, text=button_text, width=5, style='TButton')
    button.grid(row=row_index, column=col_index, padx=5, pady=5)
    button.bind('<Button-1>', lambda e, button=button: button_click(button['text']))
    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

# Create clear and delete buttons
clear_button = ttk.Button(root, text="Clear", width=10, style='TButton')
clear_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
clear_button.bind('<Button-1>', clear)

delete_button = ttk.Button(root, text="Delete", width=10, style='TButton')
delete_button.grid(row=5, column=2, columnspan=2, padx=10, pady=10)
delete_button.bind('<Button-1>', delete)

# Set dark theme
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', background='#333333', foreground='white')
style.configure('TFrame', background='#282828')
style.configure('TEntry', background='#333333', foreground='white')

root.mainloop()
if char == '=':
        calculate()
        else:
        entry.insert(tk.END, char)