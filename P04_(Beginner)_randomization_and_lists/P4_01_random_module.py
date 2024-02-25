'''
Instructions
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised and spelt exactly like e.g. Heads, not heads.

You should generate a random number, either 0 or 1.
Then use that number to print out Heads or Tails.
e.g. 1 means Heads 0 means Tails

'''

#Solution###############################################################################################################

import random

test_seed = int(input("Create a seed number: "))
random.seed(10)

random = random.randint(0, 1)

if random == 1:
    print("Heads")
else:
    print("Tails")
