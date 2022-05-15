# Step - 3

import pygame
import random

# Initializing the pygame
pygame.init()

# create the screen by providing Width = 800 and Height = 600
screen = pygame.display.set_mode((800, 600))

# Title and Icon of the window
pygame.display.set_caption("Space Invaders")

# Loading our ugo.png image as an icon of the pygame window
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('Player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')

# Randomly moving our enemy in the X and Y direction
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 40 # Moving down the enemy by 40 pixels


def player(x, y):
    # We are drawing our player image on to our screen using blit
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    # We are drawing our enemy image on to our screen using blit
    screen.blit(enemyImg, (x, y))


# Game Loop
running = True
while running:
    # Filling our black background with RGB colours inside a tuple (0,0,0)
    screen.fill((0, 0, 0))

    """
    Moving our player using keystroke is an event
    so, for that we have to enter in the below for loop
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:  # Pressing any key on the keyboard
            print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                # Decreasing the X coordinate moves the player in left direction
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                # Increasing the X coordinate moves the player in Right direction
                playerX_change = 0.3

        if event.type == pygame.KEYUP:  # Removing our fingers from the keys # means spaceship will remain
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # Making X coordinate 0 to stop the player from moving
                playerX_change = 0

    # Doing changes in the player's X coordinate
    playerX += playerX_change

    # Setting Boundaries to our game player
    # So, that player donot go outside the boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change
    # Setting Boundaries to our game enemy
    if enemyX <= 0:
        enemyX_change = 0.3 # When it strikes 0 then it starts moving in the positive direction
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3 # When it strikes end of the wall i.e 736 then it starts moving in the negative direction
        enemyY += enemyY_change

    player(playerX, playerY)  # Function calling
    enemy(enemyX,enemyY) # Function calling

    pygame.display.update()  # updating
