import pygame
import random

# Initialization
pygame.init()
# Creating screen
screen = pygame.display.set_mode((600, 600))

# Title and Icon
pygame.display.set_caption("Alien Annihilation")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

# ADDING IMAGE BACKGROUND
bg = pygame.image.load("bg.jpg")

# ADDING Player Image
spaceship = pygame.image.load("spaceship.png")
spX = 270  # X POSITION OF SPACESHIP
spY = 500  # Y POSITION OF SPACESHIP
spX_vel = 0  # CHANGE VALUE OF X VALUE

# ADDING ENEMY IMAGE
enemy = pygame.image.load("enemy.png")
enemyX = random.randint(0, 536)  # X POSITION OF SPACESHIP
enemyY = random.randint(0, 200)  # Y POSITION OF SPACESHIP
enemyX_vel = 1  # CHANGE VALUE OF X VALUE
enemyY_vel = 20  # CHANGE VALUE OF Y VALUE


def player(x, y):
    screen.blit(spaceship, (x, y))  # Blits means to draw


def alien(x, y):
    screen.blit(enemy, (x, y))  # DRAW THE ENEMY


# Active Flag
playing = True

# Game Loop
while playing:
    # Background
    screen.fill((0, 0, 0))  # RGB VALUE
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        # Keystroke
        if event.type == pygame.KEYDOWN:  # This will work if you press any key in keyboard
            if event.key == pygame.K_LEFT:  # If you pressed left key
                spX_vel = -3
            if event.key == pygame.K_RIGHT:  # IF you pressed right key
                spX_vel = 3

        if event.type == pygame.KEYUP:  # IF you released the key
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  # If you released left key
                spX_vel = 0

    spX += spX_vel  # to move the spaceship

    if spX <= 0:  # set the position of the player to 0 to create a boundary
        spX = 0
    elif spX >= 536:  # set the position of the player to 536 to create a boundary
        spX = 536

    enemyX += enemyX_vel  # to move the enemy

    if enemyX <= 0:  # set the position of the enemy to 0 to create a boundary
        enemyX_vel = 1
        enemyY += enemyY_vel
    elif enemyX >= 536:  # set the position of the enemy to 536 to create a boundary
        enemyX_vel = -1
        enemyY += enemyY_vel

    player(spX, spY)  # DRAW THE SPACE SHIP
    alien(enemyX, enemyY)  # DRAW THE ENEMY
    pygame.display.update()  # To display the background

pygame.quit()
