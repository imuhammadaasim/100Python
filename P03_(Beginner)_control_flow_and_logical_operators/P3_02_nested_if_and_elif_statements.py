'''
Instructions
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv

Warning you should round the result to the nearest whole number.
The interpretation message needs to include the words in bold from the interpretations above.
e.g. underweight, normal weight, overweight, obese, clinically obese.
'''

#Solution###############################################################################################################

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2, 2)
print(bmi)

if bmi < 18.5:
    print("You are Underweight")
elif bmi < 25:
    print("You have a Normal weight")
elif bmi < 30:
    print("You are Overweight")
elif bmi < 35:
    print("You are Obese")
else:
    print("You are Clinically Obese")
