# Split string method

import random

# This function will create a list separated by comma

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# I don't know how many names will be typed so I used the len() function to count it

numb_items = len(names)

# Using a random function and it will give me a number
# I used numb_items - 1 because index starts at 0

sortednumbertopay = random.randint(0, numb_items - 1)

# Picking who's going to pay

personwhowillpay = names[sortednumbertopay]

print(f"{personwhowillpay} is going to pay the bill today!")
