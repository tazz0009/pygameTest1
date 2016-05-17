# pygame_draw.py
"""
Example code for the draw module

"""

import pygame
from math import pi

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Setthe width and height of the screen [width, height]
size = (400, 300)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")

# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ------------ Main Program Loop ------------
while not done:

    # --- Limit to 60 frames per second
    clock.tick(60)

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

    # --- Drawing code should go here
    # line(Surface, color, start_pos, end_pos, width=1)
    pygame.draw.line(screen, GREEN, [0,0], [50,30], 5)
    # lines(Surface, color, closed, pointlist, width=1)
    pygame.draw.lines(screen, BLACK, False, [[0,80], [50,90], [200, 80], [220, 30]], 5)
    # aaline(Surface, color, startpos, endpos, blend=1)
    pygame.draw.aaline(screen, GREEN, [0, 50], [50, 80], False)
    pygame.draw.aaline(screen, GREEN, [0, 60], [50, 90], True)
    # rect(Surface, color, Rect, width=0)
    pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)
    pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])
    # ellipse(Surface, color, Rect, width=0)
    pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2)
    pygame.draw.ellipse(screen, RED, [300, 10, 50, 20])
    # polygon(Surface, color, pointlist, width=0)
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)
    # arc(Surface, color, Rect, start_angle, stop_angle, width=1)
    pygame.draw.arc(screen, BLACK,[210, 75, 150, 125], 0, pi/2, 2)
    pygame.draw.arc(screen, GREEN,[210, 75, 150, 125], pi/2, pi, 2)
    pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi,3*pi/2, 2)
    pygame.draw.arc(screen, RED,  [210, 75, 150, 125], 3*pi/2, 2*pi, 2)
    # circle(Surface, color, pos, radius, width=0)
    pygame.draw.circle(screen, BLUE, [60, 250], 40)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


# Close the window and quit.
pygame.quit()
