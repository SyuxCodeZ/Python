import pygame
import random

pygame.init()

# Set up the display in full-screen mode
screen_info = pygame.display.Info()
display_width = screen_info.current_w
display_height = screen_info.current_h
gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

block_size = 10

font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_Score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    gameDisplay.blit(value, [0, 0])

def our_snake(block_size, snake_list):
    for XnY in snake_list:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

def message_to_screen(msg, color):
    screen_text = font_style.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    snake_List = []
    Length_of_snake = 1

    food_x = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            Your_Score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, red, [food_x, food_y, block_size, block_size])
        snake_Head = []
        snake_Head.append(lead_x)
        snake_Head.append(lead_y)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                gameOver = True

        our_snake(block_size, snake_List)
        Your_Score(Length_of_snake - 1)

        pygame.display.update()

        if distance(snake_Head[0], snake_Head[1], food_x, food_y) < 20:
            food_x = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
            Length_of_snake += 1

        pygame.time.Clock().tick(15)

        if Length_of_snake == 100:  # Check if score reaches 100
            gameOver = True
            gameExit = True

    pygame.quit()
    quit()

gameLoop()