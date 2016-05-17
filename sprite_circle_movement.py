# sprite_circle_movement.py

"""
 Move a sprite in a circle.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""

import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen_width = 700
screen_height = 400
block_width = 20
block_height = 15

class Block(pygame.sprite.Sprite):
    """
    This class represents the ball that moves in a circle.
    """

    def __init__(self, color, width, height):
        """
        Constructor. Pass in the color of the block,
        and its x and y position.
        """
        # Call the parent class (Sprite) Constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimentions of the image
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

        # Instance variables that control the edges of where we bounce
        self.center_x = 0
        self.center_y = 0
        self.angle = 0
        self.radius = 0
        self.speed = 0.05

    def update(self):
        """
        Called each frame.
        """

        # Move block down one pixel
        self.rect.x = self.radius * math.sin(self.angle) + self.center_x
        self.rect.y = self.radius * math.cos(self.angle) + self.center_y
        self.angle += self.speed


class Player(pygame.sprite.Sprite):
    """
    Class to represent the player.
    """
    def __init__(self, color, width, height):
        """
        Create the player image.
        """
        # Call the parent class (Sprite) Constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimentions of the image
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()


    def update(self):
        pos = pygame.mouse.get_pos()

        if pos[0] > screen_width - block_width:
            player.rect.x = screen_width - block_width
        else:
            player.rect.x = pos[0]

        if pos[1] > screen_height - block_height:
            player.rect.y = screen_height - block_height
        else:
            player.rect.y = pos[1]


# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode([screen_width, screen_height])

# This is a list of 'sprites'. Each block in the program is
# added to this list. The list is managed by a class called 'Group'.
block_list = pygame.sprite.Group()

# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    # This represents a block
    block = Block(BLACK, block_width, block_height)

    # Set a random location for the block
    block.center_x = random.randrange(screen_width)
    block.center_y = random.randrange(screen_height)
    # Random radius from 10 to 200
    block.radius = random.randrange(10, 200)
    # Random start angle from 0 to 2pi
    block.angle = random.random() * 2 * math.pi
    # radians per frame
    block.speed = 0.008
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

# Create a RED player block
player = Player(RED, block_width, block_height)
all_sprites_list.add(player)

# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0


# ------------ Main Program Loop ------------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing  commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # Calls update() method on every sprite in the list
    all_sprites_list.update()

    # See if the player block has collided with anything.
    # spritecollide(sprite, group, dokill, collided = None)
    block_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    for block in block_hit_list:
        score += 1
        print(score)

    all_sprites_list.draw(screen)

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
