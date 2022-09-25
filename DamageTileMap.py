from tilemap import TileMap
from DamageTile import DamageTile
class DamageTileMap(TileMap):
    def __init__(self, screen):
        super(DamageTileMap, self).__init__(screen)
    def AddTile(self, texture, percentsY, isBottom, percentcX, isRight, kw, kh,damage = 3):
        tile = DamageTile(self.screen, texture, percentsY, isBottom, percentcX, isRight, kw, kh, damage)
        self.tilemap.add(tile)