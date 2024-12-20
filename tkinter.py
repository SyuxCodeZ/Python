import tkinter as tk
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
root.configure(bg='#222222')

# Create the entry field
entry = tk.Entry(root, width=35, borderwidth=5, bg='#333333', fg='white')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# ... (rest of the button layout and style configuration)

# Implement advanced functions using math module
def sin():
    try:
        angle = float(entry.get())
        result = math.sin(math.radians(angle))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# ... (similarly implement other functions like cos, tan, log, etc.)

# Add buttons for advanced functions
sin_button = ttk.Button(button_pad, text="sin", width=5, style='TButton')
sin_button.grid(row=4, column=0, padx=5, pady=5)
sin_button.bind('<Button-1>', sin)

# ... (add buttons for other advanced functions)

root.mainloop()