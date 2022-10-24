import pygame

def init_map(width, height):

    # Initialize pygame
    pygame.init()

    #create the screen
    screen = pygame.display.set_mode((width, height))

    #màu nền
    screen.fill((255,255,255))
    pygame.display.update()
    return screen

