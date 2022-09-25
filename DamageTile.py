from tile import Tile
class DamageTile(Tile):
    def __init__(self,screen, texture, percentsY, isBottom, percentcX, isRight, kW,kh,damage = 3):
        super(DamageTile, self).__init__(screen, texture, percentsY, isBottom, percentcX, isRight, kW,kh)
        self.damage = damage