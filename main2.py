import pygame

#Initialize the pygame
pygame.init()

screen = pygame.display.set_mode((800,600))

#background
bg = pygame.image.load('bg-03.png')
# Ttile and Icon
pygame.display.set_caption("My first Game")
icon = pygame.image.load('computer-game.png')
pygame.display.set_icon(icon)


running = True
while running:

    screen.blit(bg,(0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False






