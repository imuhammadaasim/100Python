'''
Instructions
You are going to write a program that calculates the highest score from a List of scores.

Important you are not allowed to use the max or min functions

Hint
Think about the logic before writing code. How can you compare numbers against each other to see which one is larger?
'''

#### Solution ##########################################################################################################

students_score = input("Enter students score: ").split()

for n in range(0, len(students_score)):
    students_score[n] = int(students_score[n])

print(students_score)

highest_score = 0
for score in students_score:
    if score > highest_score:
        highest_score = score
print(f"The high score is : {highest_score}")