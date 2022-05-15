# Step - 2
import pygame

# Initializing the pygame
pygame.init()

# create the screen by providing Width = 800 and Height = 600
screen = pygame.display.set_mode((800,600))

# Title and Icon of the window
pygame.display.set_caption("Space Invaders")

# Loading our ugo.png image as an icon of the pygame window
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('Player.png')

# Giving X and Y axis where we want to positioned our image
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

    """
    Moving our player using keystroke is an event
    so, for that we have to enter in the below for loop
    """

    # Increasing and decreasing the X and Y coordinates moves our player
    # We are increasing the palyerX and playerY coordinates by a very samll value
    # So, that we can see our player

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN: # Pressing any key on the keyboard
            print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                # Decreasing the X coordinate moves the player in left direction
                playerX_change-= 0.3
            if event.key == pygame.K_RIGHT:
                # Increasing the X coordinate moves the player in Right direction
                playerX_change += 0.3

        if event.type == pygame.KEYUP: # Removing our fingers from the keys # means spaceship will remain
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # Making X coordinate 0 to stop the player from moving
                playerX_change = 0

    # Doing changes in the player's X coordinate
    playerX+= playerX_change

    # Setting Boundaries to our game player
    if playerX <=0:
        playerX = 0 # If player is going beyond origin then take it back to the origin
    elif playerX >=736: # 800-64 = 736 where 64 pixels is the size of our player
        playerX = 736

    player(playerX,playerY) # Function calling

    pygame.display.update() # updating

