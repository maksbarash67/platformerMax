"""
Создать класс со следующей структурой наследования: Entity -> Sprite -> Player
Entity должно иметь следующие свойства и методы:
    методы: update - информация об обновлении, blit - информация об отрисовки
    свойства: name (название объекта)

Sprite должно иметь следующие свойства и методы:
    методы: get_image, get_rect - получение данных свойств
    свойства: rect (просто строка), image (просто строка)

Player должно иметь следующие свойства и методы:
    методы: go, jump, hit (урон)
    свойства: damage, health

Методы необходимо сделать асбтрактными (т.е. просто print с информацией о том, что происходит)
Создать объект Player и вызвать все методы у него.
"""


class Entity:
    def __init__(self,name):
        self.name = name
    def update(self):
        print("Обновление кадров")
    def Blit(self):
        print("Отрисовка картинки")
class Sprite(Entity):
    def __init__(self,rect,image,name):
        super(Sprite, self).__init__(name)
        self.rect = rect
        self.image = image
    def get_image(self):
        return self.image
    def get_rect(self):
        return self.rect
class Player(Sprite):
    def __init__(self,name,rect,image,damage,health):
        super(Player, self).__init__(name,rect,image)
        self.damage = damage
        self.health = health
    def Go(self):
        print("Игрок идёт")
    def Jump(self):
        print("Игрок прыгает")
    def Hit(self):
        print("Игрок наносит урон")
player = Player("Nil26","fd","tipo",23,41)
player.update()
player.Blit()
player.get_rect()
player.get_image()
player.Hit()
player.Go()
player.Jump()