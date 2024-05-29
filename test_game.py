from members import *
from gameobjects import *
import pytest

#Daniel Huynh, March 20th 2024, CS302, Karla Fant, Program 4/5. This Program is an adventure game that allows the user to 
#pick their path down the tree for a random outcome. 
#this file is a testing suite for the main functions of the game

#test armor effects
#test avatar functions
@pytest.fixture
def avatar_instance():
    return Hero("TestDummy")

#Basic Player Function Tests
def test_add_backpack(avatar_instance):
    avatarbag = avatar_instance.get_backpack()
    backpacksize= len(avatarbag)

    avatar_instance.add("woe", 1)

    assert len(avatarbag) == backpacksize + 1
    assert 'woe' in avatarbag
    assert avatarbag['woe'] == 1

#Adding Armor
def test_add_armor(avatar_instance):
    avatarbag = avatar_instance.get_armorbag()
    bagsize= len(avatarbag)

    avatar_instance.addarmor(WoodenPlate, 1)

    assert len(avatarbag) == bagsize + 1
    assert WoodenPlate in avatarbag
    assert avatarbag[WoodenPlate] == 1

#Adding Potions
def test_add_potion(avatar_instance):
    potionbag = avatar_instance.get_pouch()
    bagsize= len(potionbag)

    avatar_instance.addpotion(red_potion,1)

    assert len(potionbag) == bagsize + 1
    assert red_potion in potionbag
    assert potionbag[red_potion] == 1

#Test Attack
def test_playerattack(avatar_instance):
    enemy =Monster("joe", 10, 5)
    avatar_instance.attack(enemy)
    assert enemy.get_health() == 10-5

#Test Armor
def test_armor(avatar_instance):
    avatar_instance.set_armor(WoodenPlate)
    noob = Hero("joe")
    wolf= Monster("Wolf", 10, 10)
    wolf.attack(noob)
    wolf.attack(avatar_instance)
    avatar_instance.armoreffect()
    assert noob.get_hp() == 90
    assert avatar_instance.get_hp() == 95

'''def test_playerheal():
    ben = Hero("ben")
    ben.sethealth(10)
    ben.heal(green_potion)
    assert ben.get_hp() == 60
'''
#Test Monster Functions
def test_Entityattack(avatar_instance):
    Joe = Monster("Joe", 10, 5)
    Joe.attack(avatar_instance)
    assert avatar_instance.get_hp() == 95

#Test Crackhead Drug Donation
def test_overdose(avatar_instance):
    avatar_instance.hp = 10
    Kyle = Crackhead("Kyle", 5)
    Kyle.givefent(avatar_instance)
    assert avatar_instance.get_hp() == 0

def test_drug(avatar_instance):
    avatar_instance.sethealth(10)
    Kyle = Crackhead("Kyle", 5)
    Kyle.giveperc(avatar_instance)
    assert avatar_instance.get_hp() == 15


