import pygame
import sys
from player import Player
from tile import Tile
from tilemap import TileMap
class testAnimation():
    def __init__(self):
        # инициализация движка
        pygame.init()

        # создание экрана и установка размеров
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        pygame.display.set_caption("testAnim")


        self.tilemap = TileMap(self.screen).GetTileMap()
        self.player = Player(self.screen,self.tilemap)

    def Start(self):
        while True:
            # Чекаем события
            self.ChekEvents()
            # Обновляем лодки
            self.player.Update()

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

    def ChekUp(self, event):
        if event.key == pygame.K_d:
            self.player.right = False
        elif event.key == pygame.K_a:
            self.player.left = False


    def UpdateScreen(self):
        self.screen.fill((44,240,0))
        self.player.Blitme()
        for tile in self.tilemap.sprites():
            tile.Blitme()
        pygame.display.flip()

game = testAnimation()
game.Start()