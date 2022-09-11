from Item import Item
class Player:
    def __init__(self,money,lvl):
        self.money = money
        self.lvl = lvl
        self.inventory = [Item("Алмаз")]

    def ChekItem(self,name):
        for item in self.inventory:
            if item.name == "JetPack":
                return True
        return False

