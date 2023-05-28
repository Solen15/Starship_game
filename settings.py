class Settings:
    """Settings class"""

    def __init__(self):
        """ Initialization static game's settings """
        # Screen settings
        self.fleet_direction = None
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (150, 150, 150)

        self.screen_limit_width = 1200
        self.screen_limit_height = 800

        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_number = 10

        # enemies settings
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1

        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def set_window_limits(self):
        """ set limits of ship movement"""
        self.screen_limit_width = self.screen_width
        self.screen_limit_height = self.screen_height

    def initialize_dynamic_settings(self):
        """ Initialization dynamic settings """
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.enemy_speed = 1.0

        # direction 1 - moving right, -1 - moving left
        self.fleet_direction = 1

        #Score settings
        self.enemy_points = 50

    def increase_speed(self):
        """ Increase speed settings """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.enemy_speed *= self.speedup_scale

        self.enemy_points = int(self.enemy_points * self.score_scale)
