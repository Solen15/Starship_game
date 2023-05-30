class GameStats:
    """ collect and track statistics """

    def __init__(self,game):
        """ Statistics initialization """
        self.settings = game.settings
        self.reset_stats()

        self.high_score = 0

    def reset_stats(self):
        """ set stats at the start of the new game """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
