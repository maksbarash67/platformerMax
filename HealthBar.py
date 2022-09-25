import pygame
from pygame.sprite import Sprite
from pygame import Rect
class HealthBar(Sprite):
    def __init__(self,screen,player):
        super().__init__()
        self.screen = screen
        self.player = player
        self.rect = Rect(0, 0, 500, 40)

    def update(self):
        self.rect.width = self.player.health * 5

    def Blitme(self):
        pygame.draw.rect(self.screen, (241,46,50), self.rect)


