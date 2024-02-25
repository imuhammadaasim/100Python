'''
Instructions
You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even
number would be 2 and the last one is 100:

Important, there should only be 1 print statement in your console output. It should just print the final total and
not every step of the calculation.

Hint
There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.
'''

#### Solution ##########################################################################################################
target = int(input("Enter a number between 0 and 1000: "))

total = 0
for num in range(1, target + 1):
    if num % 2 == 0:
        total = total + num
print(total)

#### Solution ##########################################################################################################
target = int(input("Enter a number between 0 and 1000: "))

total = 0
for num in range(2, target + 1, 2):
    total = total + num
print(total)