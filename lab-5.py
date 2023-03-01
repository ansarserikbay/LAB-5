# 1esep
# students = []
# while True:
#     name = input(" имя студента : ")
#     if name == 'q':
#         break
#     grade = int(input(" класс студента: "))
#     subject = input(" предмет студента: ")
#     students.append((name, grade, subject))
# students_sorted = sorted(students, key=lambda student: student[1])
# for student in students_sorted:
#     print(f"{student[0]} - {student[1]} класс, изучает {student[2]}")

# 2esep

# grades = {
#     'Bekzhigit': [4, 5, 5, 4],
#     'Baizhanov': [3, 4, 4, 5],
#     'Abukhan': [5, 4, 5, 4],
#     'Teshebayev': [4, 5, 4, 3]
# }
# def get_grades(name):
#     if name in grades:
#         return grades[name]
#     else:
#         return []
# name = input(' имя ученика: ')
# student_grades = get_grades(name)

# if student_grades:
#     print(f'Оценки ученика {name}: {student_grades}')
# else:
#     print(f'Ученик {name} не найден')

# 3esep

# numbers = []
# while True:
#     num = int(input("Введите целое число : "))
#     if num == 0:
#         break
#     numbers.append(num)
# sorted_nums = sorted(numbers)
# for num in sorted_nums:
#     print(num)

# # 4esep

# numbers = []
# while True:
#     num = int(input("Введите целое число : "))
#     if num == 0:
#         break
#     numbers.append(num)
# numbers.sort(reverse=True)
# print("Числа в порядке убывания:")
# for num in numbers:
#     print(num)

# 5esep

# import random

# numbers = random.sample(range(1, 50), 6)

# print(sorted(numbers))

#6esep

def is_sorted(lst):
    if all(lst[i] <= lst[i+1] for i in range(len(lst)-1)):
        return True
    elif all(lst[i] >= lst[i+1] for i in range(len(lst)-1)):
        return True
    else:
        return False
lst = input("Введите последовательность чисел через пробел: ").split()
lst = [int(x) for x in lst]

if is_sorted(lst):
    print("Список отсортирован")
else:
    print("Список не отсортирован")