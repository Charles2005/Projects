import math
import random
import pygame

# Initialization
pygame.init()
# Creating screen
screen = pygame.display.set_mode((600, 600))

# Title and Icon
pygame.display.set_caption("Alien Annihilation")
icon = pygame.image.load("Images/alien.png")
pygame.display.set_icon(icon)

# ADDING IMAGE BACKGROUND
bg = pygame.image.load("Images/bg.jpg")

# ADDING Player Image
spaceship = pygame.image.load("Images/spaceship.png")
spX = 270  # X POSITION OF SPACESHIP
spY = 500  # Y POSITION OF SPACESHIP
spX_vel = 0  # CHANGE VALUE OF X VALUE

# ADDING ENEMY IMAGE
enemy = []
enemyX = []  # X POSITION OF ENEMY
enemyY = []  # Y POSITION OF ENEMY
enemyX_vel = []  # CHANGE VALUE OF X VALUE
enemyY_vel = []  # CHANGE VALUE OF Y VALUE
num_of_enemies = random.randint(6, 10)

for i in range(num_of_enemies):  # To loop through list
    enemy.append(pygame.image.load("Images/enemy.png"))
    enemyX.append(random.randint(0, 536))  # X POSITION OF ENEMY
    enemyY.append(random.randint(0, 200))  # Y POSITION OF ENEMY
    enemyX_vel.append(1)  # CHANGE VALUE OF X VALUE
    enemyY_vel.append(20)  # CHANGE VALUE OF Y VALUE

# ADDING PLAYER BULLET
bullet_img = pygame.image.load("Images/bullet.png")
bulletX = 0  # X POSITION OF SPACESHIP
bulletY = 500  # Y POSITION OF SPACESHIP
bulletX_vel = 0  # CHANGE VALUE OF X VALUE
bulletY_vel = 5  # CHANGE VALUE OF Y VALUE
bullet_state = "ready"  # state of the bullet (shoot/not)

# SCORE
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

# Game Over
game_over_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    score1 = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score1, (x, y))


def game_over():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (100, 250))


def player(x, y):
    screen.blit(spaceship, (x, y))  # Blits means to draw


def alien(x, y, i):
    screen.blit(enemy[i], (x, y))  # DRAW THE ENEMY


def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


def collision(bulletX, bulletY, enemyX, enemyY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    return False


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
            if event.key == pygame.K_SPACE:  # IF you pressed SPACE key
                if bullet_state == "ready":
                    # Get the current x coordinate of the spaceship
                    bulletX = spX
                    bullet_fire(bulletX, bulletY)

        if event.type == pygame.KEYUP:  # IF you released the key
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  # If you released left key
                spX_vel = 0

    spX += spX_vel  # to move the spaceship

    if spX <= 0:  # set the position of the player to 0 to create a boundary
        spX = 0
    elif spX >= 536:  # set the position of the player to 536 to create a boundary
        spX = 536

    for i in range(num_of_enemies):
        # Game Over
        if enemyY[i] > 275:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over()
            break

        enemyX[i] += enemyX_vel[i]  # to move the enemy

        if enemyX[i] <= 0:  # set the position of the enemy to 0 to create a boundary
            enemyX_vel[i] = 1
            enemyY[i] += enemyY_vel[i]
        if enemyX[i] >= 536:  # set the position of the enemy to 536 to create a boundary
            enemyX_vel[i] = -1
            enemyY[i] += enemyY_vel[i]
        # Collision
        is_collision = collision(bulletX, bulletY, enemyX[i], enemyY[i])
        if is_collision:
            bulletY = 500
            bullet_state = "ready"
            score += 5
            enemyX[i] = random.randint(0, 536)  # X POSITION OF ENEMY
            enemyY[i] = random.randint(0, 200)  # Y POSITION OF ENEMY

        alien(enemyX[i], enemyY[i], i)  # DRAW THE ENEMY

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 500
        bullet_state = "ready"

    if bullet_state == "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_vel

    player(spX, spY)  # DRAW THE SPACE SHIP
    show_score(textX, textY)

    pygame.display.update()  # To display the background

pygame.quit()
