import pygame
import random


#this is a comment
#this is a comment
#this is a comment
#this is a comment

pygame.init()
# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
bg = pygame.image.load('bg-03.png')

# Title and Icon
pygame.display.set_caption("My First Game")
icon = pygame.image.load('computer-game.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('warrior.png')
playerX = 70
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('giant.png')
enemyX = random.randint(50, 700)
enemyY = 385
enemyX_change = 0.3
enemyY_change = 0


# Slash ready - you cant see slash
slashImg = pygame.image.load('slash.png')
slashX = 50
slashY = 490
slashX_change = 10
slashY_change = 0
slashstate = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def swordslash(x,y):
    global slashstate
    slashstate = "slash"
    screen.blit(slashImg, (x + 16, y + 10))


# Game Screen Loop
running = True
while running:
    #   RGB - Red, Green, Blue
    screen.fill((25, 18, 50))
    # background image
    screen.blit(bg,(0,0))

    # playerX += 0.1
    # print(playerX)
# function for close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if key stroke is pressed check wheater its right or left

        if event.type == pygame.KEYDOWN:
            print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -1
                print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
                print("Right arrow is pressed")
            if event.key == pygame.K_SPACE:
                swordslash(playerX,slashX)
                print("Spacebar is pressed")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                print("Keystroke has been released")

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    #  5 = 5 - 0.1
    # Check Boundaries of Warrior
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 726:
        playerX = 726

        # Enemy Movement

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3

    elif enemyX >= 726:
        enemyX_change = -0.3

 # Slash Movement
    if slashstate == "slash":
        swordslash(playerX,slashX)
        slashX -= slashX_change




    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
