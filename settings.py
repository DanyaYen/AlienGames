class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (0, 0, 54)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 6
        self.bullet_height = 30
        self.bullet_color = (139, 0, 255)
        self.bullets_allowed = 9

        # Alien settings
        self.fleet_drop_speed = 10

        # Game settings
        self.speedup_scale = 1.5
        self.score_scale = 1.5
        self.difficulty = 'normal'

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.3
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

        
        self.initialize_dynamic_settings()