'''
Instructions
You are going to write a program which will select a random name from a list of names.
The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

one Line splits the string names_string into individual names and puts them inside a List called names.
For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

'''

#Solution###############################################################################################################

import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# get the total number of items in the list
num_items = len(names)

# generate random numbers between 0 and last index
random_choice = random.randint(0, num_items - 1)

# pick out random person from list of names using random number
who_will_pay = names[random_choice]

print(f'{who_will_pay} is going to buy the meal today!')

