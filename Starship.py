import sys

import pygame


class Starship:
    """Main class of the game"""

    def __init__(self):
        """Game initialization"""
        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Starship")

        # Background color
        self.bg_color = (150, 150, 150)

    def run_game(self):
        """Launch main loop for the game"""
        while True:
            # wait for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw the screen after each pass through the loop
            self.screen.fill(self.bg_color)

            # make updated screen visible
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    Starship().run_game()
