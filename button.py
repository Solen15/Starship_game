import pygame.font

class Button:
    """ A class for creating buttons """

    def __init__(self, game, msg):
        """ Button's initialization """
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (30, 130, 30)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.msg = msg
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """ show msg at the center of button """
        self.msg_image = self.font.render(msg, True, self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """ Draw blank button and msg """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def update_screen_size(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.rect.center = self.screen_rect.center
        self._prep_msg(self.msg)