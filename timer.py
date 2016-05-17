# timer.py
"""
 Show how to put a timer on the screen

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

font = pygame.font.Font(None, 25)

frame_count = 0
frame_rate = 60
start_time = 90

# ----- Main Program Loop -----
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Set the screen background
    screen.fill(WHITE)

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

    # --- Timer going up ---
    # Calculate total seconds
    total_seconds = frame_count // frame_rate

    # Divide by 60 to get total minutes
    minutes = total_seconds // 60

    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60

    # Use python string formatting to format in leading zeros
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

    # Blit to the screen
    text = font.render(output_string, True, BLACK)
    screen.blit(text, [250, 250])

    # --- Timer going down ---
    # Calculate total seconds
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0

    # Divide by 60 to get total minutes
    minutes = total_seconds // 60

    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60

    # Use python string formatting to format in leading zeros
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

    # Blit to the screen
    text = font.render(output_string, True, BLACK)
    screen.blit(text, [250, 280])

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1

    # Limit frames per second
    clock.tick(frame_rate)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()
