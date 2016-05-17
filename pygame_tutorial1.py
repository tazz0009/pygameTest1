# pygame_tutorial1.py

import pygame
from pygame.locals import *

pygame.init()
width = 640
height = 480

title = pygame.display.set_caption("Pygame Tutorial 1")
screen = pygame.display.set_mode((width, height))
GameImage = pygame.image.load("route.png")
screen.blit(GameImage, (0,0))
pygame.display.update()
