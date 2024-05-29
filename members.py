#Daniel Huynh, March 20th 2024, CS302, Karla Fant, Program 4/5. This Program is an adventure game that allows the user to 
#pick their path down the tree for a random outcome. 

# This file holds my core hierarchy, player class, armor/weapon/potion clas, and other functions that make each entity fill their purpose
import random
import time

#Avatar Class
class Hero:
    def __init__(self, name):
        self.__name = name
        self.__hp = 100
        self.__maxhp = 100
        self.__armor = None



        # Weapons
        self.__weapon = None
        #Inventory
        self.__backpack={}

        #Armor Bag
        self.__armorbag={}

        #Potion Inventory
        self.__pouch = {}

    #Add Weapon to Inventory
    def add(self, item, quantity):
        if item in self.__backpack:
            self.__backpack[item] += quantity
        else:
            self.__backpack[item] = quantity
  
    #Add Potion to Inventory
    def addpotion(self, item, quantity):
        if item in self.get_pouch():
            self.__pouch[item] += quantity
        else:
            self.__pouch[item] = quantity
   
    #Add Armor to Inventory
    def addarmor(self, armor, quantity):
        if armor in self.__armorbag:
            self.__armorbag[armor] += quantity
        else:
            self.__armorbag[armor] = quantity

    #Attack Monsters
    def attack(self, opp):
            damage = self.get_weapon().damage
            if damage >= opp.get_health():
                opp.sethealth(0)
            else:
                opp.sethealth(opp.get_health() - damage)
            return opp
    
    #Heal function Addition operator overload, this will increase our health
    def __add__(self, health_increase):
        if isinstance(health_increase, int):
            new_hp = min(self.__hp + health_increase, self.__maxhp)
        if isinstance(health_increase, Heal):
            new_hp = min(self.__hp + health_increase.health, self.__maxhp)
        self.sethealth(new_hp)
        return self
    
    #Potion Inventory Subtraction Operator Overload, this will remove one potion from inventory when used
    def __sub__(self, heal_name):
        self.__pouch[heal_name] -= 1
        return self
    #Display Inventory
    def displaybag(self):
        if len(self.__backpack) ==0:
            print("\nYou currently have no exra weapons")
        for weapon, quantity in self.__backpack.items():
            print(f"{weapon.name} x{quantity}")
    #Display Potions
    def displaypouch(self):
        print("\n")
        if len(self.__pouch) ==0:
            print("You currently have no potions")
        for Heal, quantity in self.get_pouch().items():
            print(f"{Heal.name} x{quantity}")
    
    #Display Armors
    def displayarmor(self):
        if len(self.__armorbag) ==0:
            print("\nYou currently have no exra armor")
        for weapon, quantity in self.__armorbag.items():
            print(f"{weapon.name} x{quantity}")

    #Healing with potion
    def heal(self, potion):
        # Convert the potion variable to a string
        potion_str = str(potion.name)  # Assuming potion has a 'name' attribute

        for heal_name, quantity in self.get_pouch().items():
            if heal_name.name.lower() == potion_str.lower():  # Case-insensitive comparison
                if quantity >= 1:
                    self + potion
                      # Assuming potion has a 'health' attribute
                    # Decrement the quantity of the used potion in the pouch
                    self - heal_name
                    print("\nPotion Consumed..\nHp:", self.get_hp(),"/",self.get_maxhp())
                    return self.get_hp()

        print(f"You don't have any {potion_str} potions left.")
        return self.get_hp()       
    
    #Armor Benefits Function
    def armoreffect(self):
        self + self.get_armor().hp
   
    #Switch Weapon
    def switchweapon(self):
        # Check if the weapon name is in the backpack
        weapon_found = False
        if len(self.__backpack) <1:
            print("You dont have any extra weapons")
            return
        while not weapon_found:
            self.displaybag()
            new_weapon = input("What item would you like to switch to?:")

            for weapon in self.__backpack:
                if new_weapon.lower() == weapon.name.lower():  # Case-insensitive comparison
                    weapon_found = True
                    print("Switched weapon to",weapon.name)
                    self.set_weapon(weapon)          
            if not weapon_found:
                print("Invalid weapon name, type exactly as shown with spaces")
    
    #Switch Armor
    def switcharmor(self):
        # Check if the armor name is in the inventory
        armor_found = False
        if len(self.__armorbag) <1:
            print("You dont have any extra armor")
            return
        while not armor_found:
            self.displayarmor()
            new_armor = input("What armor would you like to switch to?:")

            for armor in self.__armorbag:
                if new_armor.lower() == armor.name.lower():  # Case-insensitive comparison
                    armor_found = True
                    print("Switched armor to",armor.name)
                    self.set_armor(armor)          
            if not armor_found:
                print("Invalid armor name, type exactly as shown with spaces")
    #Invenory Display
    def displayhelper(self):
     picked= False
     while picked is not True:
        choice =input("\n\n1. display avatar stats\n2. display potion pouch\n3. display weapons\n4. display armors\n5. exit ")
        if choice == '1': #Avatar stats
            print("\n\nName:", self.get_name(),"\nHp:", self.get_hp(),"/", self.get_maxhp(),"\nWeapon:",self.get_weapon().name, "\nArmor:",self.get_armor().name)
            input("\n\nENTER TO CONTINUE")
            

        if choice=='2': #Potion Inventory
            self.displaypouch()
            input("\n\nENTER TO CONTINUE")
            
            
        if choice =='3': #Weapon Inventory
            self.displaybag()
            print('\n')
            input("\n\nENTER TO CONTINUE")
            
            
        if choice =='4': #Armor inventory
            self.displayarmor()
            print('\n')
            input("\n\nENTER TO CONTINUE")
            
        if choice =='5': #Exit menu
            picked = True
      
    #Getters
    def get_backpack(self):
         return self.__backpack
    def get_armorbag(self):
        return self.__armorbag
    def get_pouch(self):
        return self.__pouch
    def get_weapon(self):
        return self.__weapon
    def get_name(self):
        return self.__name
    def get_hp(self):
        return self.__hp
    def get_maxhp(self):
        return self.__maxhp
    def get_armor(self):
        return self.__armor
    #Setters
    def sethealth(self, newhp):
        self.__hp = newhp
    def set_weapon(self, weaponnew):
        self.__weapon = weaponnew
    def set_armor(self, newarmor):
        self.__armor = newarmor
    
#Weapon, found in the game
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    
#Potions, found in the game
class Heal:
    def __init__(self, name, hp):
        self.name = name
        self.health = hp
    
#Armor, found in the game
class Armor:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

#Entity Base Class, we will come across these in the game
class Entity:
   def __init__(self, name, hp, prompt):
       self.__name = name
       self.__hp = hp
       self.__prompt = prompt
    # Getters
   def get_health(self):
    return self.__hp
   def get_name(self):
    return self.__name
   def prompt(self):
       print(self.__prompt)
   
   # Setters
   def sethealth(self, newhp):
       self.__hp = newhp
    
#Derived Class 1, Players have a possibility of taking damage   
class Monster(Entity):
    def __init__(self, name, hp, damage, prompt):
        super().__init__(name, hp, prompt)
        self.__damage = damage
    
    #Attacks our player
    def attack(self, opp):
        if self.__damage >= opp.get_hp():
                opp.sethealth(0)
        else:
                opp.sethealth(opp.get_hp()- self.__damage)
        return opp
    # Damages our weapon randomly
    def biteweapon(self, opp):
        opp.getweapon().damage -=2
    
    #Increases monsters damage randomly
    def rage(self):
        self.__damage += 2  
    #Getter
    def get_damage(self):
        return self.__damage
       
#Derived Class 2, Players get healed
class Friend(Entity):
    def __init__(self, name, hp,gift, prompt):
        super().__init__(name, hp, prompt)
        self.__gift = gift
    def givegift(self, opp):
        if isinstance(self.getgift(), Heal):
            print(self.getgift().name, " has been added to your inventory")
            opp.addpotion(self.getgift(), 1)
            
        elif isinstance(self.getgift(), Weapon):
            print(self.getgift().name, " has been added to your inventory")
            opp.add(self.getgift(), 1)
        elif isinstance(self.getgift(), Armor):
            print(self.getgift().name, " has been added to your inventory")
            opp.addarmor(self.getgift(), 1)
    def telljoke(self):
        jokes = [
            "\nWhy don't scientists trust atoms? Because they make up everything!\n",
            "\nWhy did the scarecrow win an award? Because he was outstanding in his field!\n",
            "\nWhat do you call fake spaghetti? An impasta!\n",
            "\nWhy did the bicycle fall over? Because it was two-tired!\n",
            "\nWhat do you call cheese that isn't yours? Nacho cheese!\n"
        ]
        joke = random.choice(jokes)
        return joke
    #These will be the first thing our friend says when we find them
    def speak(self, opp):
        speak = [
            "Long time no see "+ opp.get_name()+"... Here you're gonna need this :)",
            "What are you doing down here "+ opp.get_name()+" its dangerous.. Take this",
            "Good to see you "+opp.get_name()+". This will help your journey",
            "Never thought I'd see you again "+ opp.get_name()+".. Here take this",
        ]
        sentence = random.choice(speak)
        print(self.get_name(),": ",sentence)
    #Getters
    def getgift(self):
        return self.__gift

#Derived Class 3, players can take a risk and either get healed or die if they are laced
class Crackhead(Entity):
    def __init__(self, name, hp, prompt):
        super().__init__(name, hp, prompt)
    #Randomized Functions that will either kill or heal our player
        
    # Player Killing Function
    def givefent(self,opp):
         time.sleep(1)
         print("Your Drugs Were Laced With Fentanyl.\n ")
         time.sleep(1)
         opp.sethealth(0)
    # Player Healing Function
    def giveperc(self, opp):
         time.sleep(1)
         print("Your Drugs Give A Sense Of Euphoria.")
         time.sleep(1)
         print("You feel much stronger")
         opp + 5
    # Drug Giving Function
    def givedrugs(self, opp):
        if random.random() < 0.6:  # 60% chance for health
            self.giveperc(opp)
        else:
            self.givefent(opp)

    def tweak(self):
        speak = [
            "AAAHAAHAHAHA",
            "HI FRIEND",
            "WANT SOME PERCS?",
            "HHEHEHEHSA",
            "FASDADALKAD"
        ]
        sentence = random.choice(speak)
        print(self.get_name(),": ",sentence) 

    def rejection(self, opp):
        speak = [
            f"You're so boring {opp.get_name()}",
            f"Your loss {opp.get_name()}",
            f"DO you ever have fun {opp.get_name()}",
            f"{opp.get_name()} your life must be so boring",
            f"YOU'RE SUCH A NERD {opp.get_name()} ADSALJFNFK"
        ]
        sentence = random.choice(speak)
        print(self.get_name(),": ",sentence) 


    
