import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """ Class to create enemies """
    def __init__(self, game):
        """ initialize enemy """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load('images/enemy_ship.bmp')
        self.rect = self. image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        """ move enemies"""
        self.x += self.settings.enemy_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """ returns True if enemy is at the edge"""
        screen_rect = self.screen.get_rect()
        return(self.rect.right >=screen_rect.right) or (self.rect.left <= 0)
