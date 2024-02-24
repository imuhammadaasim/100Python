'''
Instructions
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of some's weight taking into account their height.
e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv

Warning you should convert the result to a whole number.
'''

#Solution###############################################################################################################

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi1 = weight_as_int / height_as_float ** 2

# or using multiplication and PEMDAS
bmi2 = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi1)

print(bmi_as_int)
