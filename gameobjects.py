from members import* 
#Daniel Huynh, March 20th 2024, CS302, Karla Fant, Program 4/5. This Program is an adventure game that allows the user to 
#pick their path down the tree for a random outcome. 

# This file creates the objects found in the game, weapons, armor and potions. these all effect the difficulty of the game
#Weapon Objects
WoodenSword = Weapon("Wooden Sword", 500)
StoneSword = Weapon("Stone Sword", 10)
IronSword = Weapon("Iron Sword", 15)
SteelSword = Weapon("Steel Sword",  30)
#Potion Objects
red_potion = Heal("Red Potion",20)
blue_potion = Heal("Blue Potion",25)
green_potion = Heal("Green Potion",50)
#Armor Objects
WoodenPlate = Armor("Wooden Plate", 5)
StonePlate = Armor("Stone Plate", 20)
SteelPlate = Armor("Steel Plate", 30)