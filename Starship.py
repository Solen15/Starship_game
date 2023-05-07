import sys

import pygame

from settings import Settings
from ship import Ship

class Starship:
    """Main class of the game"""

    def __init__(self):
        """Game initialization"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Starship")

        self.ship = Ship(self)

    def run_game(self):
        """Launch main loop for the game"""
        while True:
            # wait for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw the screen after each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.draw()

            # make updated screen visible
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    Starship().run_game()
