#!/usr/bin/env python3
# Ex02:
# Create a "Player" class which can have a 'type', heath points, attack points and defense points
# The type is between 'warrior', 'magus', and 'paladin'
# Default values:
# - Warrior: 50 HP, 10 ATK, 10 DEF
# - Magus: 40 HP, 20 ATK, 5 DEF
# - Paladin: 55 HP, 15 ATK, 8 DEF
# Each player can attack. The received damage must be (Player ATK - Enemy DEF)


class Player:
    def __init__(self):
        pass


def main():
    warrior = Player("warrior")
    magus = Player("magus")
    paladin = Player("paladin")
    warrior.attack(magus)
    magus.attack(paladin)
    paladin.attack(warrior)
