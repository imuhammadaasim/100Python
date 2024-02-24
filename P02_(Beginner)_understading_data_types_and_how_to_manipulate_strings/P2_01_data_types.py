'''
Instructions
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

Warning. Your program should work for different inputs. e.g. any two-digit number.
'''

#Solution###############################################################################################################

two_digit_number = input("Type a two digit number: ")

# Checking the data type of two_digit_number
print(type(two_digit_number))

# Getting the first and second digits using subscripting then converting string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Adding the two digits together
two_digit_number = first_digit + second_digit

print(two_digit_number)
