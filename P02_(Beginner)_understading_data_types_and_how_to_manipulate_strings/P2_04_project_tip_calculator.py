print("Welcome to the tip calculator")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip you want to give? "))
people = int(input("How many people to split the bill? "))

total_tip = (tip / 100) * bill
total_bill = bill + total_tip
per_person_bill = total_bill / people

print(f"Each person should pay: ${round(per_person_bill, 2)}")