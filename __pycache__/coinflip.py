import pygame

pygame.init()

# ... (rest of your code using pygame functions)

import tkinter as tk
from tkinter import ttk
import random
import pygame

def flip_coin():
    coin_sides = ["Heads", "Tails"]
    result = random.choice(coin_sides)
    result_label.config(text=result)

    # Play a coin flip sound effect
    pygame.mixer.init()
    sound = pygame.mixer.Sound("coin_flip_sound.wav")  # Replace with your sound file
    sound.play()

    # Optionally, you can add animation here using tkinter's canvas or other animation techniques

# Create the main window
root = tk.Tk()
root.title("Coin Flip Simulator")
root.configure(bg='#222222')

# Create the result label
result_label = ttk.Label(root, text="", font=("Arial", 24), foreground="white", background="#222222")
result_label.pack(pady=20)

# Create the flip button
flip_button = ttk.Button(root, text="Flip Coin", style="TButton", command=flip_coin)
flip_button.pack(pady=10)

# Set dark theme
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', background='#333333', foreground='white')
style.configure('TLabel', background='#222222', foreground='white')

root.mainloop()