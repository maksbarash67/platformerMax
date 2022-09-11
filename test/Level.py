from Player import Player
from Item import Item
lvl = int(input("Введите уровень:"))
money = int(input("Введите кол-во монет:"))
item = input("Введите обьект:")
player = Player(money,lvl)
item1 = Item(item)
player.inventory.append(item1)
if ((player.lvl <= 9 and player.money > 10000) or (player.lvl >= 10 and player.money >= 200)) and player.ChekItem("Jetpack"):
    print("Вы прошли уровень")
else:
    print("Вы не прошли уровень")