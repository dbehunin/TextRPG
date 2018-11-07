from Player import Player
from Enemy import Enemy
from Battle import battle
from ItemList import ItemList

text = "Items/items.txt"
player = Player()
enemy = Enemy()
#testbattle = battle()

#testbattle.main(player, enemy)

Items = ItemList(text)
print(Items.getItem("Dagger").getName())
