'''
Instructions
You are going to write a program that calculates the average student height from a List of heights.


Important You should not use the sum() or len() functions in your answer. You should try to replicate their
functionality using what you have learnt about for loops.
'''

#### Solution ##########################################################################################################

student_heights = input("Input the list of student heights: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

# for loop for the sum() function
total_height = 0
for height in student_heights:
    total_height = total_height + height

# for loop for the len() function
total_students = 0
for student in student_heights:
    total_students = total_students + 1

avg_height = round(total_height / total_students)
print(f"Average height of the students is {avg_height}")