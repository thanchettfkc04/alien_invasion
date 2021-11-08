class GameStats():
    """Track điểm"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.score = 0
        self.level = 1

        #High score should never be rest
        self.high_score = 0


        # Ban đầu chưa cho bắt đầu game
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit

