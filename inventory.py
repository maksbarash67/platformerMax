import pygame
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
        self.cells = self.CreateCells()

    def CreateArray(self):
        for i in range(8):
            self.items.append([])
            for j in range(10):
                self.items[i].append(None)

    def CreateCells(self):
        tmpcells = [] # временный список ячеек

        #  Генерация 80 ячеек 100x100 px
        for i in range(8):
            tmpcells.append([])
            for j in range(10):
                cell = Cell(self.screen,i,j, 100, 100)
                tmpcells[i].append(cell)

        # выравнивание ячеек относительно инвентаря - левый верхний угол инвентаря
        for sublist in tmpcells:
            for cell in sublist:
                cell.rect.left = self.rect.left
                cell.rect.top = self.rect.top

        # Размещение временных ячеек
        for sublist in tmpcells:
            for cell in sublist:
                cell.rect.x += 100 * cell.j
                cell.rect.y += 100 * cell.i

        # Создание ячеек на основе временных
        for sublist in tmpcells:
            for cell in sublist:
                center = cell.rect.center
                cell.rect.width = 80
                cell.rect.height = 80
                cell.rect.center = center

        return tmpcells

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
        for sublist in self.cells:
            for cell in sublist:
                cell.blitme()


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
    """ Класс ячейки \n
        i,j - координаты ячейки,
        width, height - высота и ширина ячейки"""
    def __init__(self, screen, i, j, width, height):
        super(Cell, self).__init__()
        self.rect = Rect(0,0, width, height)
        self.screen = screen
        self.i = i
        self.j = j

    def blitme(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)