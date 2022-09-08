import pygame
from tile import Tile
class TileMap:
    def __init__(self,screen):
        self.screen = screen
        self.tilemap = pygame.sprite.Group()
        self.AddTile("platform.png",12,True,2,True)
        self.AddTile("platform.png", 12, True, 2, False)
        self.AddTile("platform.png", 43, False, 30, True)
        self.AddTile("platform.png", 30, True, 10, True)
        self.AddTile("platform.png", 30, True, 10, False)
        self.AddTile("platforma_dlya_igri.png",-10,True,0,True)
        self.AddTile("platforma_dlya_igri.png", -10, True, 0, False)
    def AddTile(self, texture, percentsY, isBottom, percentcX, isRight):
        tile = Tile(self.screen, texture, percentsY, isBottom, percentcX, isRight)
        self.tilemap.add(tile)
    def GetTileMap(self):
        return self.tilemap
