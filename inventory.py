import  pygame
from pygame.sprite import Sprite
from pygame.rect import Rect

class Inventory(Sprite):
    def __init__(self,screen):
        super(Inventory, self).__init__()
        self.items = []
        self.CreateArray()
        self.rect = Rect(0, 0, 1000, 800)
        self.screen = screen
        self.PosInventory()

    def CreateArray(self):
        for i in range(6):
            self.items.append([])
            for j in range(10):
                self.items[i].append(None)

    def IsFull(self):
        emptyCount = 0
        for sublist in self.items:
            for item in sublist:
                if item == None:
                    emptyCount += 1

        if emptyCount == 0:
            return True
        else:
            return False

    def PosInventory(self):
        screenRect = self.screen.get_rect()
        self.rect.center = screenRect.center

    def AddItem(self,item):
        self.items.append(item)

    def Blitme(self):
        pygame.draw.rect(self.screen, (0,114,97), self.rect)




class Item(Sprite):
    def __init__(self, screen, texture, name, price):
        super(Item, self).__init__()
        self.texture = texture
        self.name = name
        self.price = price
        self.screen = screen
        self.IN_INVENTORY = False

        self.rect = Rect(0, 0, 10, 10)

    def InInventory(self):
        self.IN_INVENTORY=True
        self.rect.width = 30
        self.rect.height = 30


    def Blitme(self):
        pygame.draw.rect(self.screen, (241, 46, 50), self.rect)

class Cell(Sprite):
    def __init__(self, screen):
        super(Cell, self).__init__()
        self.screen = screen