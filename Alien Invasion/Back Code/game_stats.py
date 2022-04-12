class GameStats():
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_settings):
        """Initials statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state
        self.game_active = False
        # High score should never be reset
        self.file = "High score.txt"
        with open(self.file) as file_o:
            self.high_score = file_o.read()
            self.high_score = int(self.high_score)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
