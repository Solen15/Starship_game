import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from score import Score
from button import Button
from ship import Ship
from bullet import Bullet
from enemy import Enemy


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

        self.stats = GameStats(self)
        self.sb = Score(self)

        # The call to Ship() requires one argument: an instance of Starship.The self argument here refers to
        # the current instance of Starship.This is the parameter that gives Ship access to the game’s resources,
        # such as the screen object. We assign this Ship instance to self.ship.
        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self._create_fleet()

        self.game_active = True

        self.play_buttom = Button(self, "Play")

    def run_game(self):
        """Launch main loop for the game"""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_enemies()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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
        self.enemies.draw(self.screen)

        self.sb.show_score()

        if not self.game_active:
            self.play_buttom.draw_button()
        # make updated screen visible
        pygame.display.flip()

    def _set_fullscreen(self):
        """ change between window and screen mode"""
        if self.fullscreen_mode:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
            self.fullscreen_mode = False
        else:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.fullscreen_mode = True
        self._restart_game(True)

    def _fire_bullet(self):
        """ Create new bullet and add it to the bullet Group """
        if len(self.bullets) < self.settings.bullets_number:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """ control number of bullets and update its position"""
        self.bullets.update()

        # remove disappeared bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_enemy_collisions()

    def _check_bullet_enemy_collisions(self):
        """ check if bullets hit enemies """
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)

        if collisions:
            for enemies in collisions.values():
                self.stats.score += self.settings.enemy_points * len(enemies)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.enemies:
            self._restart_game(False)
            self.settings.increase_speed()

            self.stats.level += 1
            self.sb.prep_level()

    def _restart_game(self, update_ship_position):
        self.bullets.empty()
        self.enemies.empty()
        self._create_fleet()
        self.ship.update_screen_size(self)
        if update_ship_position:
            self.ship.update_position()
            self.stats.score = 0
        self.play_buttom.update_screen_size(self)

    def _create_fleet(self):
        """ create fleet of enemies """
        enemy = Enemy(self)
        enemy_width, enemy_height = enemy.rect.size
        screen_width, screen_height = self.screen.get_rect().width, self.screen.get_rect().height

        current_x, current_y = enemy_width, enemy_height
        while current_y < (screen_height - 4 * enemy_height):
            while current_x < (screen_width - 2 * enemy_width):
                self._create_enemy(current_x, current_y)
                current_x += 2 * enemy_width

            current_x = enemy_width
            current_y += 2 * enemy_height

    def _create_enemy(self, current_x, current_y):
        new_enemy = Enemy(self)
        new_enemy.x = current_x
        new_enemy.rect.x = current_x
        new_enemy.rect.y = current_y
        self.enemies.add(new_enemy)

    def _update_enemies(self):
        """ update fleet's position"""
        self._check_fleet_edged()
        self.enemies.update()

        # look for enemy-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.enemies):
            self._ship_hit()

        self._check_enemies_bottom()

    def _check_fleet_edged(self):
        """ check position fleet's position and change direction"""
        for enemy in self.enemies.sprites():
            if enemy.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for enemy in self.enemies.sprites():
            enemy.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """ ship being hit by the enemy """
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self._restart_game(True)
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_enemies_bottom(self):
        """ check if any enemies have reached the bottom"""
        for enemy in self.enemies.sprites():
            if enemy.rect.bottom >= self.settings.screen_height:
                # the same as if ship got hit
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos):
        """ start new game if play_button was pressed """
        button_clicked = self.play_buttom.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.game_active = True
            self._restart_game(True)

            pygame.mouse.set_visible(False)



if __name__ == '__main__':
    Starship().run_game()
