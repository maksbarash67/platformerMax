import pygame.image
from pygame.sprite import Sprite


class Tile(Sprite):
    def __init__(self, screen, texture, percentsY, isBottom, percentcX, isRight):
        super().__init__()
        self.screen = screen
        self.screenrect = self.screen.get_rect()
        self.image = pygame.image.load(f"images/{texture}")
        self.rect = self.image.get_rect()
        self.PosY(percentsY, isBottom)
        self.PosX(percentcX, isRight)

    def PosY(self, percents, isBottom=True):
        screenHeight = self.screen.get_height()
        pixels = (percents / 100) * screenHeight

        if isBottom == True:
            self.rect.bottom = self.screenrect.bottom + pixels * -1
        else:
            self.rect.top = self.screenrect.top + pixels * 1

    def PosX(self, percents, isRight=True):
        screenWidth = self.screen.get_width()
        pixels = (percents / 100) * screenWidth

        if isRight == True:
            self.rect.right = self.screenrect.right + pixels * -1
        else:
            self.rect.x = self.screenrect.left + pixels * 1

    def Blitme(self):
        self.screen.blit(self.image, self.rect)