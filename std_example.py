
students_list=  [
    ["Alice", 85, 90, 78],  # average grade ?
    ["Bob", 72, 88, 91],
    ["Charlie", 90, 87, 85],
    ["Diana", 60, 65, 70]]

# point 01

for std in students_list:  # each std is a list ?
    # I need to calculate average of grade for each student ?
    avg = 0
    no_of_courses = 0
    total_of_grades = 0
    for grade in std:
        if isinstance(grade, int) or isinstance(grade, float):
            total_of_grades += grade
            no_of_courses += 1

    avg = total_of_grades/no_of_courses
    std.append(avg)
    print(std)


print(f"------------ {students_list} ")

print()

##############33 point number 02

print(students_list)
top_student = students_list[0]
print(top_student)

for student in students_list:
    if student[-1] > top_student[-1]:
        top_student = student

print(f"top student is {top_student}")




############3 point no 3
#  3- sort the students by their average, desc .
sorted_students = []
sorted_students.append(students_list[0])
for stdd in students_list[1:]:
    if stdd[-1] > sorted_students[0][-1]:
        sorted_students.append(stdd)
    else:
        sorted_students.insert(0, stdd)

# print(sorted_students)
sorted_students.reverse()
print(sorted_students)

#### point number 4 -->
for ss in students_list:
    if ss[-1] >= 85:
        ss.append("Excellent")
    elif ss[-1] >= 75:
        ss.append("Very Good")
    elif ss[-1] >= 65:
        ss.append("Good")
    elif ss[-1] >= 60:
        ss.append("Pass")
    else:
        ss.append("Fail")

print(students_list)


####### total for all students
total_class = 0
for sd in students_list:
    total_class += sd[-2]

avg_class = total_class/len(students_list)
print(avg_class)









