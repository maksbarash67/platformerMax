from  inventory import Inventory
import pygame
import sys
from player import Player
from tile import Tile
from tilemap import TileMap
from DamageTileMap import DamageTileMap
from  HealthBar import  HealthBar
class testAnimation():
    def __init__(self):
        # инициализация движка
        pygame.init()

        # создание экрана и установка размеров
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN )

        pygame.display.set_caption("testAnim")


        self.tilemap = TileMap(self.screen)
        self.damageTileMap = DamageTileMap(self.screen)
        self.SetTiles()
        self.player = Player(self.screen,self.tilemap.GetTileMap(), self.damageTileMap.GetTileMap())
        self.healthbar = HealthBar(self.screen,self.player)
        self.inventory = Inventory(self.screen)
        self.inventoryUpdate = False


    def SetTiles(self):
        self.damageTileMap.AddTile("damage.png", 38, True, 30, False, 100, 25)

        self.tilemap.AddTile("platform.png", 12, True, 2, True, 2.738944365192582, 11.73913043478261)
        self.tilemap.AddTile("platform.png", 12, True, 2, False, 2.738944365192582, 11.73913043478261)
        self.tilemap.AddTile("platform.png", 43, False, 30, True, 2.738944365192582, 11.73913043478261)
        self.tilemap.AddTile("platform.png", 30, True, 10, True, 2.738944365192582, 11.73913043478261)
        self.tilemap.AddTile("platform.png", 30, True, 10, False, 2.738944365192582, 11.73913043478261)
        self.tilemap.AddTile("platforma_dlya_igri.png", -10, True, 0, True, 1.443609022556391, 6.75)
        self.tilemap.AddTile("platforma_dlya_igri.png", -10, True, 0, False, 1.443609022556391, 6.75)



    def Start(self):
        while True:
            # Чекаем события
            self.ChekEvents()
            # Обновляем лодки
            self.player.Update()
            self.healthbar.update()
            # Обновляем экран
            self.UpdateScreen()

    def ChekEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.ChekDown(event)
            elif event.type == pygame.KEYUP:
                self.ChekUp(event)

    def ChekDown(self, event):
        if event.key == pygame.K_d:
            self.player.right = True
        elif event.key == pygame.K_a:
            self.player.left = True
        elif event.key == pygame.K_SPACE:
            if self.player.IsJumping == False:
                self.player.StartJumping()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_e:
            self.inventoryUpdate = not self.inventoryUpdate


    def ChekUp(self, event):
        if event.key == pygame.K_d:
            self.player.right = False
        elif event.key == pygame.K_a:
            self.player.left = False

    def UpdateInvatoryIfNeed(self):
        if self.inventoryUpdate:
            self.inventory.Blitme()

    def UpdateScreen(self):
        self.screen.fill((44,240,0))
        self.player.Blitme()
        self.tilemap.Blit()
        self.healthbar.Blitme()
        self.damageTileMap.Blit()
        self.UpdateInvatoryIfNeed()
        pygame.display.flip()

game = testAnimation()
game.Start()