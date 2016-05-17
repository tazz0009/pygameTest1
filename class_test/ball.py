# ball.py
import pygame

class Ball():
    def __init__(self):
        self.x = 0
        self.y = 0

        self.change_x = 0
        self.change_y = 0

        self.size = 10

        self.color = [255, 255, 255]

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)
