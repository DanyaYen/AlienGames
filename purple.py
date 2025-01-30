import pygame # type: ignore
from pygame.sprite import Sprite # type: ignore

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.radius = self.settings.bullet_width // 2
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = int(self.y)

    def draw_bullet(self):
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.radius)