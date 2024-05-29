from members import *
from RBTree import *
# Daniel Huynh, March 20th 2024, Program 4/5, CS302 Karla Fant, This program is a adventure based game where the user starts at the top of
# the cave and works down to the bottom to save the hostage named jessica. the player will find new items that will help their journey
# the entities are crackhead, monster, and friend. they all behave differently and the 3 items in the inventory are weapons, armor, and potions

#this file is the main file where the user operates the main menu to start the game, display the tree/recent players or retrieve 
#exception handling can be foun in RBTree.py insert functions and more
while True:
  
    tree= RedBlackTree()
    playergame = Game(tree)
    tree.initialize()
    gamemode = 1
    
    while gamemode == 1:
        print("\n  ***Project Caveman***  \n")
        print("(1) Begin Journey (2) Display Options (3) Retrieve Location (4) End Program")
        choice = input(">>>")
        if choice == '1':
            while True:
                name = input("What is your name?")
                if name != None and name != "":
                    break
                else:
                    print("\nError entering name\n")
            player = Hero(name)
            playergame.setplayer(player)
            playergame.welcome(player)
            player.set_armor(WoodenPlate)
            player.set_weapon(WoodenSword)

            playergame.startgame(player, tree.root)

        elif choice == '2':
            while True:
                pick=input("\n(1) Display Tree (2) Recent Players")
                if pick != None and pick != "":
                    break
                else:
                    print("\nplease pick valid option\n")
            pick = int(pick)
            if pick ==1:
                tree.display()
            if pick ==2:
                playergame.displayplayers()
        elif choice == '3':
            tree.retrieve()
        elif choice =='4':
            gamemode =2
     
    if gamemode ==2:
        print("\nClosing The Applciation\n")
        break


