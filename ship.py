import pygame


class Ship:
    """ Ship class"""

    # The __init__() method of Ship takes two parameters: the self reference and a reference to
    # the current instance of the Starship class. This will give Ship access to all the game
    # resources defined in Starship. We then assign the screen to an attribute of Ship , so we can
    # access it easily in all the methods in this class.
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
