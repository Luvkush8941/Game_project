# Step-4
# Making a bullet and we will fired that also
import pygame
import random

# Initializing the pygame
pygame.init()

# create the screen by providing Width = 800 and Height = 600
screen = pygame.display.set_mode((800, 600))

# Background image
background = pygame.image.load('background_image.jpg')

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
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.5
enemyY_change = 40  # Moving down the enemy by 40 pixels

# Bullet
# Ready - You can't see the bullets on the screen
# Fire - The bullets are currently moving

bulletImg = pygame.image.load('Bullet.png')
bulletX = 0
bulletY = 480  # Bullet is fired from the players level
bulletX_change = 0
bulletY_change = 0.6
bullet_state = "ready"


def player(x, y):
    # We are drawing our player image on to our screen using blit
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    # We are drawing our enemy image on to our screen using blit
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # drawing the bullets on the screen but disappears when it back to while loop
    screen.blit(bulletImg, (x + 16, y + 10))  # We had added 16 and 10 so, that bullet can be fired
    # from the middle of the spaceship


# Game Loop
running = True
while running:
    # Filling our black background with RGB colours inside a tuple (0,0,0)
    screen.fill((0, 0, 0))

    """
    Moving our player using keystroke is an event
    so, for that we have to enter in the below for loop
    """

    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:  # Pressing any key on the keyboard
            print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.7
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.7

            # Whenever we pressed the Space button then bullet will be fired
            if event.key == pygame.K_SPACE:
                # If the bullet state is ready then only we can fire the bullet by pressing Spacebar
                if bullet_state == "ready":
                # As bullet was moving with the spaceship
                # i.e we had given the initial X coordinate of the player to the bullet
                         bulletX = playerX
                         fire_bullet(playerX, bulletY)

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
        enemyX_change = 0.5  # When it strikes 0 then it starts moving in the positive direction
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.5  # When it strikes end of the wall i.e 736 then it starts moving in the negative direction
        enemyY += enemyY_change

    # Bullet Movement

    # Whenver we fired 1 bullet then we cannot fire another one
    # So, to rectify that we  had written the below code
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        # Here we are sending the X coordinate of the bullet which will remain same till the bullet cross the upper wall
        fire_bullet(bulletX, bulletY)  # Function calling
        bulletY -= bulletY_change

    player(playerX, playerY)  # Function calling
    enemy(enemyX, enemyY)  # Function calling

    pygame.display.update()  # updating
