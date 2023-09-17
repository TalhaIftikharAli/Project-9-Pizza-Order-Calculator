# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 19:33:32 2023

@author: talha.i
"""

# Pizza Calculator
# 🚨 Don't change the code below 👇

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# 🚨 Don't change the code above 👆

bill = 0

# Pizza Size:
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

# Add Pepperoni:
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
else:
    bill += 0
    
# Cheese:
if extra_cheese == "Y":
    bill += 1
else:
    bill += 0
    

print(f"Your final bill is: ${bill}.")
