# -*- coding: utf-8 -*-
"""Dice Game

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bLz3lf_G6F9px2ZxcK7RNZpKmYvrFWfN
"""

import random
import time
roll_again= "yes"
while roll_again== "yes" or roll_again== "y" or roll_again== "Yes" or roll_again== "Y":
  print("\nRolling The Dice...")
  time.sleep(1)

  dice1= random.randint(1,6)
  dice2= random.randint(1,6)

  print("You rolled")
  print("Dice One:",dice1,"\nDice Two:",dice2,"\nTotal:",dice1+dice2)

  roll_again= input("Do You Want To Roll Again? (No/Yes) ")