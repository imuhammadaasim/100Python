'''
Instructions
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digits number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is **z**."

'''

#Solution###############################################################################################################

print("Welcome to Love Calculator")

name1 = input("Enter your name: ")
name2 = input("Enter their name: ")

combined_names = (name1 + name2).lower()

print(combined_names)

t = combined_names.count('t')
r = combined_names.count('r')
u = combined_names.count('u')
e = combined_names.count('e')

l = combined_names.count('l')
o = combined_names.count('o')
v = combined_names.count('v')
e = combined_names.count('e')

true = t + r + u + e
love = l + o + v + e

score = int(str(true) + str(love))

if 10 < score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")
