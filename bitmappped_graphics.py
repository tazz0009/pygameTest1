# bitmappped_graphics.py

"""
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/4YqIKncMJNs
 Explanation video: http://youtu.be/ONAK8VZIcI4
 Explanation video: http://youtu.be/_6c4o41BIms
"""

import pygame

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


    click_sound = pygame.mixer.Sound("laser5.ogg")

    background_position = [0, 0]

    background_image = pygame.image.load("saturn_family1.jpg").convert()
    player_image = pygame.image.load("player.png").convert()
    player_image.set_colorkey(BLACK)

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play()
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        screen.blit(background_image, background_position)

        player_position = pygame.mouse.get_pos()
        x = player_position[0]
        y = player_position[1]

        screen.blit(player_image, [x, y])
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

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
