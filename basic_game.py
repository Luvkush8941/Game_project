# Step - 1
import pygame

# creating our first game window
# Initializing the pygame
pygame.init()

# create the screen by providing Width = 800 and Height = 600
screen = pygame.display.set_mode((800,600))

# Pygame window will be visible till running is true
# Closing the window, moving the cursor in that window are the event
# When pygame is quit i.e pygame.quit is True then we stop the pygame window by exitting from
# this while loop

# Title and Icon of the window
pygame.display.set_caption("Space Invaders")

# Loading our ugo.png image as an icon of the pygame window
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('Player.png')
# Giving X and Y axis where we want to positioned our image
# We want our player to be positioned and to be moved much below the 600
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    # We are drawing our player image on to our screen using blit
    screen.blit(playerImg,(x,y))


# Game Loop
running  =  True
while running:
    # Filling our black background with RGB colours inside a tuple (0,0,0)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Note:
    # Always call the player after filling the screen
    # Otherwise first player is drawn then our screen is filled
    # By which we are unable to see our player.

    # Calling player here as we want our player to be displayed
    # onto the screen till we donot get exit from that particular window
    player(playerX,playerY)
    # Updating our window display for after filling background RGB colours
    # Without updating we cannot see any changes
    pygame.display.update()

