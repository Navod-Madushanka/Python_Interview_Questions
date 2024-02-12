student_heights = input("Input a list of student heights ").split()
sum_of_Heights = 0
len_of_heights = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  sum_of_Heights += student_heights[n]
  len_of_heights += 1

print(round(sum_of_Heights / len_of_heights))