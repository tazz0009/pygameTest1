# bullets.py
"""
 Show how to fire bullets.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/PpdJjaiLX6A
"""
import pygame
import random

# 정적변수 정의 -----(
# 컬러 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# 화면 사이즈 정의
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
# 정적변수 정의 -----)

# 클래스 Block 정의 -----(
class Block(pygame.sprite.Sprite):
    """
    This class represents the block.
    """
    def __init__(self, color):
        # Call the parent class (Sprite) Constructor
        super().__init__()

        self.image = pygame.Surface([20, 15])
        self.image.fill(color)

        self.rect = self.image.get_rect()

# 클래스 Block 정의 -----)
