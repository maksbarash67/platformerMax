import pygame
from pygame.sprite import Sprite
class Player(Sprite):
    def __init__(self,screen,tilemap, damageTileMap):
        super().__init__()
        self.screen = screen
        self.tilemap = tilemap
        self.damageTileMap = damageTileMap
        self.screenrect = self.screen.get_rect()

        self.Respawn()

    def Update(self):
        self.ChekDamage()
        if self.right == True and self.rect.right < self.screenrect.right:
            self._x += self.screen.get_width()/480
            self.image = pygame.image.load("images/pygame_right_2.png")
            self.image = pygame.transform.scale(self.image, (
            self.screen.get_width() / 32.0, self.screen.get_height() / 15.211267605633802))
        elif self.left == True and self.rect.left > self.screenrect.left:
            self._x -= self.screen.get_width()/480
            self.image = pygame.image.load("images/pygame_left_1.png")
            self.image = pygame.transform.scale(self.image, (
            self.screen.get_width() / 32.0, self.screen.get_height() / 15.211267605633802))
        elif (self.right == False and self.left == False) or (self.right == True and self.left == True):
            self.image = pygame.image.load("images/pygame_idle.png")
            self.image = pygame.transform.scale(self.image, (
            self.screen.get_width() / 32.0, self.screen.get_height() / 15.211267605633802))
        if self.IsJumping == True:
            if self.yisUp == True:
                self._y -= self.screen.get_height()/216
                if self._y <= self.MaxJumpHeit:
                    self.yisUp = False
                    self.yisDown = True
            if self.yisDown == True:
                if not self.ChekStopJumping():
                    self._y += self.screen.get_height()/216
                else:
                    self.yisDown = False
                    self.IsJumping = False
        elif not self.ChekStopJumping():
            if not self.ChekStopJumping():
                self._y += self.screen.get_height()/216

        self.rect.x = self._x
        self.rect.y = self._y
    def Blitme(self):
        self.screen.blit(self.image,self.rect)

    def StartJumping(self):
        self.yisUp = True
        self.IsJumping = True
        self.MaxJumpHeit = self.rect.y - self.screen.get_height()/4.695652173913043

    def Respawn(self):
        self.health = 100
        self.image = pygame.image.load("images/pygame_idle.png")
        self.image = pygame.transform.scale(self.image, (
        self.screen.get_width() / 32.0, self.screen.get_height() / 15.211267605633802))
        print(
            f"k_ширина: {self.screen.get_width() / self.image.get_width()}\nk_высота: {self.screen.get_height() / self.image.get_height()}")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screenrect.midbottom
        self.rect.y -= self.screen.get_height() / 10.8

        self._x = float(self.rect.x)
        self._y = float(self.rect.y)
        self.IsJumping = False
        self.right = False
        self.left = False
        self.yisUp = False
        self.yisDown = False
        self.MaxJumpHeit = self.rect.y - self.screen.get_height() / 4.695652173913043

    def ChekDamage(self):
        colideTile = pygame.sprite.spritecollideany(self, self.damageTileMap)

        if colideTile != None:
            self.health -= colideTile.damage
            print(self.health)
            if self.health <= 0:
                self.Respawn()


    def ChekStopJumping(self):
        colideTile = pygame.sprite.spritecollideany(self,self.tilemap)

        if colideTile != None:
            #if colideTile.rect.top == self.rect.y + 70 or (colideTile.rect.top + 5 >= self.rect.y + 70 ):
            if colideTile.rect.top == self.rect.y + self.screen.get_height()/15.42857142857143 or (colideTile.rect.top + self.screen.get_height()/216 >= self.rect.y + self.screen.get_height()/15.42857142857143 ):
                return True

        return False