# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_scores = {student:random.randint(0,100) for student in names}
# print(student_scores)
# passed_student = {student: score for (student, score) in student_scores.items() if score >= 60}
# print(passed_student)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day: (temp*9/5)+32 for (day, temp) in weather_c.items()}
#
# print(weather_f)

import pandas

student_dict = {
    "name": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    print(row["name"])
