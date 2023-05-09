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
        self.settings = starship_game.settings

        # Load the ship image
        self.image = pygame.image.load('images/Starship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # store a float for the ship's position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def draw(self):
        """Draw the ship"""

        self.screen.blit(self.image, self.rect)

    def update(self):
        """ Checking movement flags and update ship's position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def adjust_x_after_winresize(self, previous_width, new_width):
        """Change ship position after changing window/fullscreen mode"""
        self.x = self.x * new_width/previous_width
