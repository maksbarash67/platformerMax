import pygame
from pygame.sprite import Sprite
from pygame.rect import Rect
from random import randint

class Inventory(Sprite):
    def __init__(self,screen):
        super(Inventory, self).__init__()
        self.items = []
        self.CreateArray()
        self.rect = Rect(0, 0, 1000, 800)
        self.screen = screen
        self.PosInventory()
        self.cells = self.CreateCells()

    def SpawnItemTest(self):
        for i in range(74):
            item = Item(self.screen,"banana_bullet.png","banan Pulya",21)
            item.InInventory()
            self.AddItem(item)

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
        for sublist in self.items:
            for i in range(len(sublist)):
                if sublist[i] == None:
                    item.InInventory()
                    sublist[i] = item
                    return

    def Blitme(self):
        # Отрисовка области инвентаря
        pygame.draw.rect(self.screen, (0,114,97), self.rect)

        # Отрисовка ячеек
        for sublist in self.cells:
            for cell in sublist:
                cell.blitme()
                item = self.items[cell.i][cell.j]
                if item != None:
                    item.rect.center = cell.rect.center
                    item.Blitme()



class Item(Sprite):
    def __init__(self, screen, texture, name, price):
        super(Item, self).__init__()
        self.texture = texture
        self.name = name
        self.price = price
        self.screen = screen
        self.IN_INVENTORY = False

        #self.rect = Rect(0, 0, 10, 10)

        # Подгрузить картинку
        self.image = pygame.image.load(f"images/{texture}")
        self.image = pygame.transform.scale(self.image, (30, 30))
        # Получить rect картинки
        self.rect = self.image.get_rect()


    def InInventory(self):
        self.IN_INVENTORY=True
        self.image = pygame.transform.scale(self.image, (60,60))
        self.rect = self.image.get_rect()


    def Blitme(self):
        #pygame.draw.rect(self.screen, (241, 46, 50), self.rect)
        # Отрисовать картинку
       self.screen.blit(self.image,self.rect)

    def Pos(self, tile):
        self.rect.midbottom = tile.rect.midtop
        x = tile.rect.width // 2
        self.rect.x += randint(0, x) * randint(-1,1)

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