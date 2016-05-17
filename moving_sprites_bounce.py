# moving_sprites_bounce.py

"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""

import pygame
import random

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
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
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
        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0

        # Instance variables for our current speed and direction
        self.change_x = 0
        self.change_y = 0


    def update(self):
        """
        Called each frame.
        """

        # Move block down one pixel
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        # If block is too far down, reset to top of screen.
        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1
        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1


class Player(Block):
    """
    The player class derives from Block, but oberrides the 'update'
    functionality with new a movement function that will move the block
    with the mouse.
    """
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
    block.rect.x = random.randrange(screen_width-block_width)
    block.rect.y = random.randrange(screen_height-block_height)

    block.change_x = random.randrange(-3, 4)
    block.change_y = random.randrange(-3, 4)
    block.left_boundary = 0
    block.top_boundary = 0
    block.right_boundary = screen_width
    block.bottom_boundary = screen_height

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
