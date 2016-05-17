# ball_main.py

"""

"""

import pygame
from ball import Ball

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def main():
    """ Main function for the game. """
    pygame.init()

    # Set the width and height of the screen [width,height]
    size = [800, 600]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("CMSC 150 is cool")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()


    theBall = Ball()
    theBall.x = 100
    theBall.y = 100
    theBall.change_x = 2
    theBall.change_y = 1
    theBall.color = [255,0,0]

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        screen.fill(BLACK)
        theBall.move()
        theBall.draw(screen)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()

if __name__ == "__main__":
    main()
