
import pygame

class Ship:
    """ Ship class"""

    def __init__(self, starship_game):
        """Ship initialization"""
        self.screen = starship_game.screen
        self.screen_rect = starship_game.screen.get_rect()

        # Load the ship image
        self.image = pygame.image.load('images/Starship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def draw(self):
        """Draw the ship"""

        self.screen.blit(self.image, self.rect)
