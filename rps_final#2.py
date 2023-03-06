# Created by Connor Counts 
 
# import libraries

from time import sleep

from random import randint 

import pygame as pg

import os

game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
# tuples are constants and cannot be changed once stated
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# The choices that the user can choose from
choices = ["rock", "paper", "scissors"]

# Draws the text we see on the intro screen screen 
def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

# allows the cpu to randomly choose from the given choices of 0, 1, or 2
def cpu_randchoice():
    choice = choices[randint(0,2)]
    print("The computer chose " + choice)
    return choice

# allows me to use Pygame for this program
pg.init()
pg.mixer.init()

# the screen is now connected to pygame
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors...")
clock = pg.time.Clock()

# letting python know how I want to use rock, paper, and scissors in the code later
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
rock_image_rect = rock_image.get_rect()
cpu_rock_image_rect = rock_image.get_rect()

paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
cpu_paper_image_rect = paper_image.get_rect()

scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()
cpu_scissors_image_rect = scissors_image.get_rect()



start_screen = True

# Letting python know that the player_choice and cpu_choice will be the prevoiusly stated words in ""
player_choice = ""
cpu_choice = ""
running = True

while running:
    clock.tick(FPS)
    
    # if you close out of the screen, the program will stop running
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
                
        # checks for keyboard
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                print("Start Game")
                start_screen = False
        
        if event.type == pg.MOUSEBUTTONUP:
            mouse_coords = pg.mouse.get_pos()

           # Establishes the relationship between the users choice and the cpu randomly choosing another output
            print(rock_image_rect.collidepoint(mouse_coords))
            if rock_image_rect.collidepoint(mouse_coords):
                print("you clicked on rock...")
                player_choice = "rock"
                cpu_choice = cpu_randchoice()

            elif paper_image_rect.collidepoint(mouse_coords):
                print("you clicked on paper...")
                player_choice = "paper"
                cpu_choice = cpu_randchoice()
       
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("you clicked on scissors...")
                player_choice = "scissors"
                cpu_choice = cpu_randchoice()                      
            else:
                # to let the user know if what they are trying to do isn't working
                print("Theres nothing there")
    
    

    # the screens background color 
    screen.fill(BLACK)

    # waits for player to hit space bar
    if start_screen == True:
        draw_text("Press space to play rock paper scissors", 22, WHITE, WIDTH/2, HEIGHT/10)

    # allows player to choose rock paper or scissors
    if not start_screen and player_choice == "":
        rock_image_rect.x = 50
        paper_image_rect.x = 350
        scissors_image_rect.x = 550
        screen.blit(scissors_image, scissors_image_rect)
        screen.blit(paper_image, paper_image_rect)
        screen.blit(rock_image, rock_image_rect)

# below are the choices that occur when the user clicks on a certian image

    # rock vs rock = Tie
    if player_choice == "rock":
        if cpu_choice == "rock":
            rock_image_rect.x = 100
            cpu_rock_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("You Tied :|", 22, WHITE, WIDTH/2, HEIGHT/10)
    # rock vs paper = Lose
    if player_choice == "rock":
        if cpu_choice == "paper":
            rock_image_rect.x = 100
            cpu_paper_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            draw_text("You Lost :(", 22, WHITE, WIDTH/2, HEIGHT/10)
    # rock vs scissors = Win
    if player_choice == "rock":
        if cpu_choice == "scissors":
            rock_image_rect.x = 100
            cpu_scissors_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            draw_text("You Win!!! :)", 22, WHITE, WIDTH/2, HEIGHT/10)


    # paper vs paper = Tie
    if player_choice == "paper":
        if cpu_choice == "paper":
            paper_image_rect.x = 100
            cpu_paper_image_rect.x = 500
            screen.blit(paper_image, paper_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            draw_text("You Tied :|", 22, WHITE, WIDTH/2, HEIGHT/10)
    # paper vs rock = Win
    if player_choice == "paper":
        if cpu_choice == "rock":
            paper_image_rect.x = 100
            cpu_rock_image_rect.x = 500
            screen.blit(paper_image, paper_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("You Win!!! :)", 22, WHITE, WIDTH/2, HEIGHT/10)
    # paper vs scissors = Lose
    if player_choice == "paper":
        if cpu_choice == "scissors":
            paper_image_rect.x = 100
            cpu_scissors_image_rect.x = 500
            screen.blit(paper_image, paper_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            draw_text("You Lose :(", 22, WHITE, WIDTH/2, HEIGHT/10)
 
 
# scissors vs scissors = Tie
    if player_choice == "scissors":
        if cpu_choice == "scissors":
            scissors_image_rect.x = 100
            cpu_scissors_image_rect.x = 500
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            draw_text("You Tied :|", 22, WHITE, WIDTH/2, HEIGHT/10)
    # scissors vs paper = Win
    if player_choice == "scissors":
        if cpu_choice == "paper":
            scissors_image_rect.x = 100
            cpu_paper_image_rect.x = 500
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            draw_text("You Win!!! :)", 22, WHITE, WIDTH/2, HEIGHT/10)
    # scissors vs rock = Lose
    if player_choice == "scissors":
        if cpu_choice == "rock":
            scissors_image_rect.x = 100
            cpu_rock_image_rect.x = 500
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("You Lose :(", 22, WHITE, WIDTH/2, HEIGHT/10)
    pg.display.flip()

pg.quit()

""""
Sources: 
Chris Cozort, Period 6, rps.py 
"""