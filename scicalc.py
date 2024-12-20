import pygame
import tkinter as tk
from tkinter import messagebox
import random

# Initialize Pygame and Tkinter
pygame.init()

# Set up the Tkinter window for displaying the game
root = tk.Tk()
root.title("Snake Game")
root.geometry("600x500")

# Game settings
WIDTH, HEIGHT = 600, 400
SQUARE_SIZE = 20
FPS = 10
LIGHT_BLUE = (173, 216, 230)
LIME = (0, 255, 0)
PURPLE_GRAPES = (128, 0, 128)
WHITE = (255, 255, 255)

# Create Pygame window on the Tkinter canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="lightblue")
canvas.pack()

# Game variables
score = 0
snake = [(100, 100), (80, 100), (60, 100)]  # Initial snake body
direction = "RIGHT"
food = (0, 0)

# Set the font for displaying the score
score_font = pygame.font.SysFont("Arial", 20)

# Function to display the score
def display_score(score):
    canvas.create_text(300, 20, text=f"Score: {score}", fill="white", font=("Arial", 20))

# Function to draw the snake
def draw_snake(snake):
    for segment in snake:
        canvas.create_rectangle(segment[0], segment[1], segment[0] + SQUARE_SIZE, segment[1] + SQUARE_SIZE, fill=LIME)

# Function to draw food (grapes)
def draw_food(food):
    x, y = food
    # Drawing grapes as a circle (purple)
    canvas.create_oval(x, y, x + SQUARE_SIZE, y + SQUARE_SIZE, fill=PURPLE_GRAPES)

# Function to update the snake's position
def update_snake(snake, direction):
    head_x, head_y = snake[0]
    if direction == "UP":
        head_y -= SQUARE_SIZE
    elif direction == "DOWN":
        head_y += SQUARE_SIZE
    elif direction == "LEFT":
        head_x -= SQUARE_SIZE
    elif direction == "RIGHT":
        head_x += SQUARE_SIZE

    new_head = (head_x, head_y)
    snake = [new_head] + snake[:-1]  # Move the snake by adding new head and removing the last segment
    return snake

# Function to check for collisions with walls or self
def check_collisions(snake):
    head_x, head_y = snake[0]
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        return True  # Hit wall
    if (head_x, head_y) in snake[1:]:
        return True  # Hit itself
    return False

# Function to generate food at a random position
def generate_food():
    food_x = random.randint(0, (WIDTH - SQUARE_SIZE) // SQUARE_SIZE) * SQUARE_SIZE
    food_y = random.randint(0, (HEIGHT - SQUARE_SIZE) // SQUARE_SIZE) * SQUARE_SIZE
    return (food_x, food_y)

# Function to handle key presses (for snake movement)
def change_direction(event):
    global direction
    if event.keysym == "Up" and direction != "DOWN":
        direction = "UP"
    elif event.keysym == "Down" and direction != "UP":
        direction = "DOWN"
    elif event.keysym == "Left" and direction != "RIGHT":
        direction = "LEFT"
    elif event.keysym == "Right" and direction != "LEFT":
        direction = "RIGHT"

# Function to handle the game over condition
def game_over():
    messagebox.showinfo("Game Over", f"Game Over! Final Score: {score}")
    root.quit()  # Close the Tkinter window

# Main game loop
def game_loop():
    global snake, food, score, direction
    snake = update_snake(snake, direction)

    # Check for collisions
    if check_collisions(snake):
        game_over()
        return

    # Check if snake eats the food
    head_x, head_y = snake[0]
    food_x, food_y = food
    if head_x == food_x and head_y == food_y:
        score += 10
        food = generate_food()
        snake.append(snake[-1])  # Grow the snake by adding a new segment

    # Clear the canvas and redraw everything
    canvas.delete("all")
    canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="lightblue")
    draw_snake(snake)
    draw_food(food)
    display_score(score)

    # Schedule the next frame
    root.after(1000 // FPS, game_loop)

# Bind the arrow keys for snake movement
root.bind("<Up>", change_direction)
root.bind("<Down>", change_direction)
root.bind("<Left>", change_direction)
root.bind("<Right>", change_direction)

# Initialize food and start the game
food = generate_food()

# Start the game loop
game_loop()

# Start the Tkinter main loop
root.mainloop()
