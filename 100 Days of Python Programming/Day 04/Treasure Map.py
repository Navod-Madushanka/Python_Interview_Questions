row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

row_number = position[0]
column_number = position[1]

map[int(column_number)-1][int(row_number)-1] = "X"


print(f"{row1}\n{row2}\n{row3}")