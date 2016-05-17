# game_class_example.py
"""
Show the proper way to organize a game using the a game class.

Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Explanation video: http://youtu.be/O4Y5KrNgP_c
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

def collided(click_sound):
    click_sound.play()

# 클래스 Block 정의 -----(
class Block(pygame.sprite.Sprite):
    """
    플레이어가 수집해야할 블럭을 표시한다.
    """
    def __init__(self):
        """
        생성자. 블록의 색상 그리고 x, y 위치 세팅
        """
        # Call the parent class (Sprite) Constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        #b = pygame.sprite.Sprite()
        self.image = pygame.image.load("Tennisball.png")

        # Fetch the rectangle object that has the dimentions of the image
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

    def reset_pos(self):
        """
        Called when the block is 'collected' or falls off the screen.
        """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(SCREEN_WIDTH)

    def update(self):
        """
        Automatically called when we need to move the block.
        """
        self.rect.y += 1

        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()

# 클래스 Block 정의 -----)
# 클래스 Player 정의 -----(
class Player(pygame.sprite.Sprite):
    """
    This class represents the player.
    """
    def __init__(self):
        super().__init__()
        #self.image = pygame.Surface([20, 20])
        #self.image.fill(RED)
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()

    def update(self):
        """
        Update the player location.
        """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

# 클래스 Player 정의 -----)
# 클래스 Game 정의 -----(
class Game(object):
    """
    This class represents an Instance of the game. If we need to
    reset the game we'd just need to create a new Instance of this class.
    """
    def __init__(self):
        """
        Constructor. Create all our attributes and initialize the game.
        """
        self.score = 0
        self.game_over = False

        # Create sprite lists
        self.block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        # Create the block sprites
        for i in range(50):
            block = Block()
            block.rect.x = random.randrange(SCREEN_WIDTH)
            block.rect.y = random.randrange(-300, SCREEN_HEIGHT)

            self.block_list.add(block)
            self.all_sprites_list.add(block)

        self.player = Player()
        self.all_sprites_list.add(self.player)


    def process_events(self):
        """
        Process all of the events. Return a "True" if we need
        to close the window.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
        return False

    def run_logic(self, click_sound):
        """
        This method is run each time through the frame. It updates positions
        and checks for collisions
        """
        if not self.game_over:
            # Move all the sprites
            self.all_sprites_list.update()

            # See if the player block has collided with anything.
            blocks_his_list = pygame.sprite.spritecollide(self.player, self.block_list, True)

            # Check the list of collisions.
            for block in blocks_his_list:
                self.score += 1
                print(self.score)

            if len(self.block_list) == 0:
                self.game_over = True

    def display_frame(self, screen):
        """
        Display everything to the screen for the game.
        """
        screen.fill(WHITE)

        if self.game_over:
            font = pygame.font.SysFont("arial", 25)
            text = font.render("Game Over, click to restart", True, BLACK)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if not self.game_over:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()


# 클래스 Game 정의 -----)

# 클래스 main 정의 -----(
def main():
    """
    Main program function.
    """

    pygame.init()
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")
    pygame.mouse.set_visible(False)

    click_sound = pygame.mixer.Sound("laser5.ogg")

    # Create our objects and set the data
    done = False
    clock = pygame.time.Clock()

    # Create an Instance of the Game class
    game = Game()

    while not done:

        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()

        # Update object positions, check for collisions
        game.run_logic(click_sound)

        # Draw the current frame
        game.display_frame(screen)

        clock.tick(60)

    pygame.quit()

# 클래스 main 정의 -----)

if __name__ == "__main__":
    main()
