from members import *
from gameobjects import* 

#Daniel Huynh, March 20th 2024, CS302, Karla Fant, Program 4/5. This Program is an adventure game that allows the user to 
#pick their path down the tree for a random outcome. 

#This file holds our red black tree class and game class. 
#The game class is what is used to traverse down the tree and interact with each node. while the red black tree class is just for insertion, initializing, displaying and retrievals
class Game:
    def __init__(self, tree):
            self.tree = tree
            self.player = None

            self.playerlist=[]

    def setplayer(self, player1): #sets name
            self.player=player1
            self.playerlist.append(player1)
    def displayplayers(self): #displays recent player list
        print("\nRecent Players:\n")
        self.display_players_recursive(self.playerlist, 0)

    def display_players_recursive(self, playerlist, i): #recursive call
        if i == len(playerlist):
            if i == 0:
                print("There has been no players recently ")
            return
        player = playerlist[i]
        print(f"{i + 1}. {player.get_name()}")  # Assuming player has a string representation
        self.display_players_recursive(playerlist, i + 1)
        
    # Main Menu
    def mainmenu(self):
        print()
        print("(1) Enter Cave | (2) Display Path | (3) Retrieve Location | (4) End Program")
    # Beginning Starter Loot
    def welcome(self, opp):
        print("\n**For testing purposes the player has a 500 damage weapon**\n")
        time.sleep(2)
        print("\nYou walk towards the cave..")
        time.sleep(1)
        print("\nPolice Officer: Hello you must be ", opp.get_name(),", I heard you're going to help us look for jessica.\nits going to be a tough journey going down that cave.. let me give you some of my spare items")
        time.sleep(3)
        print("\nNew items have been added to your inventory","\n3x Red Potions\n2x Blue Potions\n1x Green Potion\n1x Wooden Sword \n1x WoodenPlate")
        time.sleep(1)
        print("\nGood luck solider")
        opp.addpotion(red_potion,3)
        opp.addpotion(blue_potion, 2)
        opp.addpotion(green_potion,1)
        opp.add(WoodenSword,1)
        opp.addarmor(WoodenPlate,1)
        input("\n\nENTER TO CONTINUE\n")
    #Interaction with our nodes
    def npcinteract(self, player, location):
        #Crackhead Interact
        if isinstance(location.get_data(), Crackhead):
                print("We continue down the path")
                time.sleep(2)
                print("You run into a Crackhead named ", location.get_data().get_name()," and are offered some drugs")
                time.sleep(2)
                location.get_data().tweak()
                while True:
                    decide=int(input("(1) Take the drugs offered (2) Pass on the drugs"))
                    if decide ==1:
                        print("\nYou take the drugs")
                        location.get_data().givedrugs(player)
                        break
                    if decide ==2:
                        time.sleep(1)
                        print("\nYou wisely pass on the drugs")
                        time.sleep(1)
                        location.get_data().rejection(player)
                        time.sleep(1)
                        break
                    else:
                        print("\nError. Please enter either 1 or 2.\n")
         
        #Friend Interact
        if isinstance(location.get_data(), Friend):
            print("\nWe continue down the path")
            time.sleep(1)
            print("\nYou run into a Friend named ", location.get_data().get_name())
            time.sleep(1)
            location.get_data().speak(player)
            location.get_data().givegift(player)
            if random.random() < 0.4:  # 40% chance for a joke
                location.get_data().telljoke()
            time.sleep(2)
          
        #Monster Interact
        if isinstance(location.get_data(), Monster):
            print("\nWe continue down the path")
            time.sleep(1)
            print("\nYou run into a Monster! : ", location.get_data().get_name())
            time.sleep(2)
            print("\n",location.get_data().get_name()," Starts charging at you\n")
            time.sleep(2)
            self.gamestart(player, location.get_data())
            
    # Fight Menu Extras
    def fightmenu(self, player, opp): #displays details of both player and monster
        print("Name:",player.get_name(), ' ' * 60, opp.get_name())
        print("Hp:", player.get_hp(), ' ' * 59, "Hp:", opp.get_health())
        print("Weapon:", player.get_weapon().name)
        print("Armor:", player.get_armor().name)
        print("\n(1) Attack ", ' ' * 14, "(2) Heal", ' ' * 15, "(3) View Info", ' ' * 10, " (4) Switch Weapon" ,' ' * 10,"(5) Switch Armor")
    
    #This Function holds the fight menu, this only shows up when dealing with monsters
    def gamestart(self, p1, p2): #this starts the game and allows for input
        while p2.get_health() > 0:
            if p1.get_hp() ==0:
                return
            self.fightmenu(p1, p2)
            choice = input(">>>")
            try:
                if choice == '1': #attacks
                    print('\n', p1.get_name(), " attacked ", p2.get_name())
                    time.sleep(1)
                    p1.attack(p2)
                elif choice == '2': #heals player
                    p1.displaypouch()
                    choice2 = input("\n\n(1) red potion\n(2) blue potion\n(3) green potion")
                    if choice2 == '1':
                        p1.heal(red_potion)
                    elif choice2 == '2':
                        p1.heal(blue_potion)
                    elif choice2 == '3':
                        p1.heal(green_potion)
                    else:
                        print("\nError. pick valid option\n")
                elif choice == '3':
                    p1.displayhelper()
                elif choice == '4': #switch weapon
                    p1.displaybag()
                    print("\nCurrently Equipped:", p1.get_weapon().name)
                    p1.switchweapon()
                    input("\n\nENTER TO CONTINUE")
                elif choice =='5': #switch armor
                    p1.displayarmor()
                    print("\nCurrently Equipped:", p1.get_armor().name)
                    p1.switcharmor()
                    input("\n\nENTER TO CONTINUE")
                else:
                    print("\nError. Pick valid option\n")
                self.fightmenu(p1, p2)
                time.sleep(1)
                if p2.get_health() > 0:
                    print(p2.get_name(), " attacks", p1.get_name())
                    time.sleep(1)
                    p2.attack(p1)
                    p1.armoreffect()
            except ValueError:
                print("\nError from input\n")
        if p2.get_health() == 0:
            print("\n",p2.get_name()," was slain\n")
            time.sleep(1)
    def endgame(self, opp):
        #Unique End Game Functions depending on leaf name
        time.sleep(1)
        if opp.get_name() == "Benson":
            print("\nYou cut the drops off jessica and head towards the top of the cave\n")
            time.sleep(2)
            return True
        elif opp.get_name() == "King Troll":
            print("\nKing Troll starts to wither away..\nJessica: I never thought I was gonna see another day thank you so much! \n")
            time.sleep(2)
            return True
        elif opp.get_name() == "King Tut":
            print("\njessica comes crawling out of the dungeon..\n jessica: you're a life saver..\n")
            time.sleep(2)
            return True
        elif opp.get_name() == "Johnson":
            print("\nJohnson Welcomes you to his tent with jessica getting aid\njessica:thank you so much for coming.. i've been feeling better\n")
            time.sleep(2)
            return True
        elif opp.get_name() == "Joey":
            print("\nJoey Leads you in the correct direction\n")
        elif opp.get_name() == "King Kunta":
            print("\nKing Kunta Disappears into thin air \n")
            time.sleep(2)
            return True
        elif opp.get_name() == "Lava Serpent":
            print("\nThe Lava Serpent explodes into lava and kills you and jessica\n")
            time.sleep(2)
            return False
        elif opp.get_name() == "Jourmintide":
            print("\nThe jessica walks out the opening in very poor health.. you bring the jessica to safety\n")
            print("\njessica: Please tell me my family is safe..\n")
            time.sleep(2)
            return True
            
        if opp.get_name() == "King Kunta":
            print("\nThe army releases the case and you take jessica to safety\n")
            time.sleep(2)
            return True
        if opp.get_name() == "Serpent":
            print("\nYou see jessica unconcious but still breathing.. looks like we made it just in time.\n")
            time.sleep(2)
            return True
        if opp.get_name() == "King Kong":
            print("\nJessica is knocked uncincious from the fall, but seems to be in stable condition. you take jessica to safety\n")
            time.sleep(2)
            return True
        if opp.get_name() == "Pack Leader Wolf":
            print("\nthe pack leads you to their territory with jessica visibly shaking..\njessica: please help me.. im scared.\n")
            time.sleep(2)
            return True
        if opp.get_name() == "Georgie":
            print("\nyou search the cove fo jessica..")
            time.sleep(2)
            print("You have no luck")
            time.sleep(2)
            print("\nJoe calls you from your radio..")
            time.sleep(2)
            print("\nJoe: im afraid its too late..\n")
            return False

        if opp.get_name() == "Digtoise":
            print("\nYou and jessica both fall into the pothole and die of lava\n")
            time.sleep(2)
            return False
        if opp.get_name() == "Debras Uncle":
            print("\nYou discover jessica on the floor of the basement.. we were too late.\n")
            time.sleep(2)
            return False
        if opp.get_name() == "Geodude":
            print("\nYou and jessica are both crushed by the cave.\n")
            time.sleep(2)
            return False
        if opp.get_name() == "Onyx":
            print("\nYou walk towards the light and find jessica with a torch.. seems like she's been defending her self well.\n")
            time.sleep(2)
            print("\nyou guide her to the top.\n")
            time.sleep(2)
            return True
        
    #This Function hold the actual game, players will move along the tree using this function
    def startgame(self, player, location):
        #Interaction with NPCs
        self.npcinteract(player, location)
        if player.get_hp() ==0:
            print("\nYou Died!\n")
            time.sleep(3)
            return
        location.get_data().prompt()
        time.sleep(3)
        #checks if we're at a leaf
        if location.get_left() is None and location.get_right() is None:
            #invokes unique ending depending on leaf
            if self.endgame(location.get_data()) is True:
                print("\nYou win")
            else:
                print("\nYou lose")
            return
        #Displays user stats
        print("location:", location.get_location())
        print("\nName:", player.get_name(), " \nHp:", player.get_hp(),"/",player.get_maxhp())
        #Displays left and right options
        if location.get_left() is not None and location.get_right() is not None:
            print("\nLeft:", location.get_left().get_location() , "\nRight:", location.get_right().get_location())
        elif location.get_left() is not None and location.get_right() is None:
            print("\nLeft:", location.get_left().get_location())
        else:
            print("\nRight:", location.get_right().get_location())
        print("\n")
        while True:
            try:
                while True:
                    choice =input("(1) Head Left (2) Head Right (3) Interact Inventory (4) Commit Suicide ")
                    if choice is not None:
                        break
                choice = int(choice)
                if choice ==1 and location.get_left() is not None: #traverse left and calls recursive
                    self.startgame(player,location.get_left())
                    break
                    
                elif choice ==2 and location.get_right is not None: #traverse right and calls recursive
                    self.startgame(player,location.get_right())
                    break
                elif choice ==3: #Interacts with the players inventory
                    button =int(input("\n(1) Heal Character (2) Switch Weapon (3) Switch Armor (4) View Player Info "))
                    if button ==1: #heals our character
                        print("\nHp: ", player.get_hp(),"/", player.get_maxhp())
                        player.displaypouch()
                        choice2 = input("\n(1) red potion\n(2) blue potion\n(3) green potion")
                        if choice2 == '1':
                            player.heal(red_potion)
                        if choice2 == '2':
                            player.heal(blue_potion)
                        if choice2 == '3':
                            player.heal(green_potion)
                    elif button == 2: #switches weapon
                        player.displaybag()
                        print("\nCurrently Equipped:", player.get_weapon().name, "\n")
                        player.switchweapon()
                        input("\n\nENTER TO CONTINUE")
                    elif button ==3: #switches armor
                        player.displayarmor()
                        print("\nCurrently Equipped:", player.get_armor().name,"\n")
                        player.switcharmor()
                        input("\n\nENTER TO CONTINUE")
                    elif button ==4: #Displays extras
                        player.displayhelper()
                    else:
                        print("Invalid choice or no available option. Try again.")
                elif choice ==4: #ends game early
                    print("\nYou killed yourself\n")
                    time.sleep(3)
                    return 
                    
                else:
                    print("Invalid choice or no available option. Try again.")
            except ValueError:
                print("Error occured")
            
        
class RedBlackTree:
    class TreeNode:
        def __init__(self, data, location, num):
            self.__data = data
            self.__location = location
            self.__num = num
            self.__left = None
            self.__right = None
            self.__color = 'Red'
            self.__parent = None
        # Getters
        def get_data(self):
            return self.__data
        def get_number(self):
            return self.__num
        def get_left(self):
            return self.__left
        def get_right(self):
            return self.__right
        def get_color(self):
            return self.__color
        def get_parent(self):
            return self.__parent
        def get_location(self):
            return self.__location

        # Setters
        def set_data(self, data2):
            self.__data = data2
        def set_left(self, newleft):
            self.__left =newleft
        def set_right(self, newright):
            self.__right = newright
        def set_color(self, newcolor):
            self.__color = newcolor
        def set_parent(self, newparent):
            self.__parent = newparent

    def __init__(self):
        self.root = None
        self.case1 = False  # left left case
        self.case2 = False  # right right case
        self.case3 = False  # left right case
        self.case4 = False  # right left case
   
    # Left Rotate
    def rotateLeft(self, node):
        x = node.get_right()
        y = x.get_left()
        x.set_left(node)
        node.set_right(y)
        node.set_parent(x)
        if y is not None:
            y.set_parent(node)
        return x
 
    # Right Rotate
    def rotateRight(self, node):
        x = node.get_left()
        y = x.get_right()
        x.set_right(node)
        node.set_left(y)
        node.set_parent(x)
        if y is not None:
            y.set_parent(node)
        return x
    
    #Initliaze the tree
    def initialize(self):
    
    #Early Game, Picks path
    
        self.insert(Friend("Joe", 10, green_potion, "\nWhat a sad situation, i heard jessica's family tried going in the cave to look for her but it was too dangerous.."), "Cave Entrance", 100)
    
        self.insert(Monster("Snail", 5, 1,"\nYou hear  echoing screams on the right.. what could it be? there also seems to be a quieter safer option to the left..."), "Moisty Mire", 50)
    
        self.insert(Monster("Armadillo", 15, 20,"\nYou find a hair tie on the ground.. jessica was seen wearing this. perhaps we're going in the right direction"), "Pleasant Park", 150)
    
        #Mid Game, path determines weapon/loot
        self.insert(Friend("Moe", 5, StonePlate, "\nI'm surprised you made it this far.. still no sign of jessica...\nBut bens been in the dragons den healing his wounds, its tough in there. not so sure about whats on the left.."), "Murky Swamplands",170)
        self.insert(Monster("Juvenile Wolf", 20, 5, "\nYou hear friendly chatter and laughs on the right tunnel.. maybe we could get some guidance?"), "Obsidian Hollow", 130)

        self.insert(Crackhead("Michael", 10,"\nI HAVE A REALLY GOOD FRIEND IF YOU JUST TAKE A LEFT HE WILL GIVE U LOTS OF STUFF HEHE"), "Echoing Caverns", 70)
        self.insert(Friend("koko", 10, StoneSword, "Further down theres packs of wolves.. I heard the Silent Sands is less stressful"), "Cryptic Catacombs",30)

        #End game boss fights or happy endings
    
        self.insert(Monster("Alpha Wolf", 50,20,"You feel a strong wave of heat on the right.. could that be it? theres also a strong pee like stench to the left"), "Shadowed Tunnels",20)
        self.insert(Monster("Adult Wolf", 30, 15, "\nYou hear two loud murmers on both the left and right tunnels, but the left is more high pithced and seems friendly."), "Silent Sands",40)

        self.insert(Monster("Michaels Pet Troll", 30, 30, "\nTell Michael I love him.. \n\nyou see a bright shining light to the right.. could this be the end..?"), "Cryptic Catacombs",60)
        self.insert(Friend("John", 10, IronSword, "That Michael guy has issues, I think they took a right from here"), "Johns Block", 80)

        self.insert(Friend("Security Guard Cole", 10, IronSword,"Grab yourself some coffee and relax. You're really brace for doing this."), "Safe House", 120)
    
        self.insert(Friend("Jose", 5, SteelPlate,"I've had no luck finding jessica, but I think we're close. Be careful, nobody has ever returned after going deeper than here.."), "Misty Meadow", 140)

        self.insert(Monster("Debra", 30,20,"\nDebras Janitor: Take a left my friend trust me.. Debra told me everything"), "Debras House", 160)
        self.insert(Friend("Ben", 10, SteelSword,"\nIm sure moe sent you didn't he? haha I love that guy.\n But on a serious note be careful.. i think is she's in one of these 2 areas..I saw a female bracelet on the ground."), "Dragons Den", 180)

        #Boss fights
        self.insert(Monster("Benson", 50, 20,"\nfine.. take her.. X_X"), "Bensons Tent", 18)
        self.insert(Monster("Lava Serpent", 60,20, "The fire serpent drops a key to unlock the cage..."), "Serpents Nest", 22)

        self.insert(Monster("King Troll", 40,20,"\nhehehehe fine you can have her"), "Trollworld", 35)
        self.insert(Monster("King Tut", 60,20,"\nMaybe you arent so weak after all.. "), "Dusty Dungeon", 45)

        self.insert(Crackhead("Johnson", 5,"\nOK WELL SHE'S SLEEPING IN MY TENT HAHA"), "Busted Tent", 59)
        self.insert(Friend("Joey", 5, green_potion,"\nGlad you made it safe, I've been taking care of her for the time being... Lets get out of here.\n"), "A Bright Light", 61)

        self.insert(Monster("King Kunta", 60,20,"\nKing Kuntas army surrenders and leads you to jessica"), "Moss Village", 75)
        self.insert(Monster("Serpent", 60,20,"\nYou cut open the serpents stomach"), "Serpents Nest", 83)

        self.insert(Monster("King Kong", 100,50,"\nYou walk towards king kongs hand and release his grip"), "Jungle Nest", 118)
        self.insert(Monster("Pack Leader Wolf", 60,20, "\nThe beta wolves surrender and lead you to jessica"), "Furry Frost", 122)

        self.insert(Monster("Georgie", 60,20,"\ni-i..i dont even know why you're here.."), "Georgie's Cove", 135)
        self.insert(Monster("Digtoise", 60,20, "\nA pothole starts forming and rapidly spreads"), "Digtoise's Territory", 145)

        self.insert(Monster("Geodude", 60,50, "The Cave starts crashing down"), "Rocky Road", 161)
        self.insert(Monster("Debra's Uncle", 50,25, "\nShe's in the basement... x_x"), "Debras Garage", 159)
      
        self.insert(Monster("Onyx", 60,50, "\nA sharp bright light appears out of no where, could this be the end..?"), "Obsidian Slope", 175)
        self.insert(Monster("Jourmintide", 80,50,"\nA strange opening appears.."), "Killer's Cove", 183)     

    #Insertion Function       
    def insert(self, data2, location, num):
        try:
            if self.root is None: 
                self.root = self.TreeNode(data2,location, num)
                self.root.set_color("Black")
            else:
                self.root = self.insert2(self.root, self.TreeNode(data2, location, num) )
                self.root.set_color("Black")
        except Exception as caught:
            print("Error Allocating Memory: ", caught)
            
    #Recursive Insertion Function 
    def insert2(self, root, data):
        doubleredcheck = False  # red red check

        if root == None:
            return data
        
        # Finding the correct position
        elif data.get_number() < root.get_number():
            root.set_left(self.insert2(root.get_left(), data)) # traverse left if its less than current num value
            root.get_left().set_parent(root) # set parent and case check for a double red
            if root != self.root and root.get_color() == "Red" and root.get_left().get_color() == "Red": 
                doubleredcheck = True 
        else: # traverse right if its higher than current num value
            root.set_right(self.insert2(root.get_right(), data))
            root.get_right().set_parent(root) #Set parent and case check for a double red
            if root != self.root and root.get_color() == 'Red' and root.get_right().get_color() == "Red":
                doubleredcheck = True
        
        #  double red check and black uncle check
        if doubleredcheck:
            self.doubleredfix(root, root.get_parent())

        # check if any black uncles were found
        self.testcases()
        return root
    
    def testcases(self): #Only happens when parents sibling is black
        if self.case1: #left left case, both parent and current nodes are red left child: 
            root = self.rotateLeft(root)
            root.set_color("Black")
            root.get_left().set_color("Red")
            self.case1 = False
        elif self.case2: #right right case, both parent and current nodes are red right childs
            root = self.rotateRight(root)
            root.set_color("Black")
            root.get_right().set_color("Red")
            self.case2 = False
        elif self.case3: #left right case, parent is a left red child and current is a right red bhild
            root.set_left(self.rotateLeft(root.get_left())) 
            root.get_left().set_parent(root) # parent gets left rotated and returns a left left relationship then solved with case 1 
            root = self.rotateRight(root)
            root.set_color("Black")
            root.get_right().set_color("Red")
            self.case3 = False
        elif self.case4: # right left case, parent is a right red child and current is a left red child. 
            root.set_right(self.rotateRight(root.get_right()))
            root.get_right().set_parent(root) # parent gets right rotated and returns a right right relationship solved with case 2
            root = self.rotateLeft(root)
            root.set_color("Black")
            root.get_left().set_color("Red")
            self.case4 = False
        return True

    def doubleredfix(self, root, parent):
        if parent.get_left() == root:
            sibling = parent.get_right()
            if sibling == None:
                return
            if sibling.get_color() == "Black": #check cases if theres a black uncle
                if root.get_left().get_color() == "Red":
                    self.case3 = True
                elif root.get_right().get_color() == "Red":
                    self.case2 = True
            else:
                sibling.set_color("Black")
                root.set_color("Black")
                if parent != self.root:
                    parent.set_color("Red")
        else:
            sibling = parent.get_left()
            if sibling == None:
                return
            if sibling.get_color() == "Black":
                if root.get_left().get_color() == "Red":
                    self.case4 = True
                elif root.get_right().get_color() == "Red":
                    self.case1 = True
            else:
                sibling.set_color("Black")
                root.set_color("Black")
                if parent != self.root:
                    parent.set_color("Red")

    #Display Helper Function
    def display(self):
        print("\nIn order traversal display:\n")
        self.display2(self.root)

    #Recursive Display Function 
    def display2(self, node):
        if node is None:
           return
        self.display2(node.get_left())
        print("\nName:",node.get_data().get_name() + "\nColor:",(node.get_color()))
        self.display2(node.get_right())
    #Retrieve Function Helper
    def retrieve(self):
        while True:
            try:
                namesearch = input("What is the name you're looking for in this tree?")
                if namesearch != None and namesearch != "":
                    break
                else:
                    print("\nError name input")
            except KeyboardInterrupt:
                print("\nKeyboard error")
                return False
        print("\nSearching..")
        time.sleep(1)
        if self.retrieve2(self.root, namesearch) is True:
            return True
        else:
            print("\nCouldnt find this name")
            return False
    def retrieve2(self, node, namesearch):
        try:
            if(node.get_left()):
                if self.retrieve2(node.get_left(), namesearch):
                    return True
            if namesearch.lower () == node.get_data().get_name().lower():
                print("\nMatch Found!")
                time.sleep(1)
                if isinstance(node.get_data(), Friend):
                    print("\nName: ", node.get_data().get_name())
                    time.sleep(1)
                    print("\nHp: ", node.get_data().get_health())
                    time.sleep(1)
                    print("\nGift: ", node.get_data().getgift().name)
                    time.sleep(1)
                    print("\nLocation: ",node.get_location()) 
                    time.sleep(1)        
                if isinstance(node.get_data(), Monster):
                    print("\nName: ", node.get_data().get_name())
                    time.sleep(1)
                    print("\nHp: ", node.get_data().get_health())
                    time.sleep(1)
                    print("\nDamage: ", node.get_data().get_damage())
                    time.sleep(1) 
                    print("\nLocation: ",node.get_location()) 
                    time.sleep(1)        
                if isinstance(node.get_data(), Crackhead):
                    print("\nName: ", node.get_data().get_name())
                    time.sleep(1)
                    print("\nHp: ", node.get_data().get_health())
                    time.sleep(1)
                    print("\nLocation: ",node.get_location()) 
                    time.sleep(1)        
                return True
            if(node.get_right()):
                if self.retrieve2(node.get_right(), namesearch):
                    return True
            return False
        except Exception as e:
            print("\nError:", e)
            return False
        