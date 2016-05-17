# bouncing_rectangle.py
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Setthe width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of the rectangle
rect_x = 50
rect_y = 50

# Speed and dirction of rectangle
rect_change_x = 5
rect_change_y = 5


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
    screen.fill(BLACK)

    # --- Drawing code should go here

    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    rect_x += rect_change_x
    rect_y += rect_change_y

    if rect_y > 450:
        rect_change_y = rect_change_y * -1
    if rect_x > 650:
        rect_change_x = rect_change_x * -1
    if rect_y == 0:
        rect_change_y = rect_change_y * -1
    if rect_x == 0:
        rect_change_x = rect_change_x * -1

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
