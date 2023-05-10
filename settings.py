
class  Settings:
    """Settings class"""

    def __init__(self):
        """Game's settings initialization"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (150, 150, 150)

        self.screen_limit_width = 1200
        self.screen_limit_height = 800

        self.ship_speed = 3#1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_number = 10

    def set_window_limits(self):
        """ set limits of ship movement"""
        self.screen_limit_width = self.screen_width
        self.screen_limit_height = self.screen_height
