import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class Starship:
    """Main class of the game"""

    def __init__(self):
        """Game initialization"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.fullscreen_mode = False
        pygame.display.set_caption("Starship")

        # The call to Ship() requires one argument: an instance of Starship.The self argument here refers to
        # the current instance of Starship.This is the parameter that gives Ship access to the game’s resources,
        # such as the screen object. We assign this Ship instance to self.ship.
        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Launch main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            # remove disappeared bullets
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """ Check keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Key pressed"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_o:
            self._set_fullscreen()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """ Key released"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """ Update image on the screen """

        # redraw the screen after each pass through the loop
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.draw()

        # make updated screen visible
        pygame.display.flip()

    def _set_fullscreen(self):
        """ change between window and screen mode"""
        previous_width = self.screen.get_rect().width
        if self.fullscreen_mode:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
            self.ship.screen_rect = self.screen.get_rect()
            self.fullscreen_mode = False
        else:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.ship.screen_rect = self.screen.get_rect()
            self.fullscreen_mode = True
        screen_rect = self.screen.get_rect()
        self.ship.adjust_x_after_winresize(previous_width = previous_width, new_width = self.screen.get_width())
        self.ship.rect.bottom = screen_rect.bottom

    def _fire_bullet(self):
        """ Create new bullet and add it to the bullet Group """
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

if __name__ == '__main__':
    Starship().run_game()
