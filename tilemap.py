import pygame
from tile import Tile
class TileMap:
    def __init__(self,screen):
        self.screen = screen
        self.tilemap = pygame.sprite.Group()

    def AddTile(self, texture, percentsY, isBottom, percentcX, isRight, kw, kh):
        tile = Tile(self.screen, texture, percentsY, isBottom, percentcX, isRight, kw, kh)
        self.tilemap.add(tile)
    def GetTileMap(self):
        return self.tilemap

    def Blit(self):
        for tile in self.tilemap.sprites():
            tile.Blitme()