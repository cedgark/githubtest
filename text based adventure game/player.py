from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]

# Start game at the reception
current_room = rooms["Reception"]

s = 0
mass = 0
for i in inventory:
    mass = inventory[s] ["mass"] + mass
    s = s + 1
