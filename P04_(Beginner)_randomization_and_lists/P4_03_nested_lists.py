line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot. Columns are A, B, & C while Rows are 1, 2, & 3")
position = input("Where do you want to put the treasure? A2? C3? B1? ")


letter = position[0].lower()
abc = ['a', 'b', 'c']
index_letter = abc.index(letter)

number = int(position[1]) - 1

map[index_letter][number] = 'X'

print(f"{line1}\n{line2}\n{line3}")


