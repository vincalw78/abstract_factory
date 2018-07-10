"""
6) Є дані
    lloyd = { "name": "Lloyd", "homework": [90.0,97.0,75.0,92.0],  "quizzes": [88.0,40.0,94.0], "tests": [75.0,90.0] }
    alice = {"name": "Alice", "homework": [100.0, 92.0, 98.0, 100.0],  "quizzes": [82.0, 83.0, 91.0], "tests": [89.0, 97.0] }
    tyler = { "name": "Tyler",  "homework": [0.0, 87.0, 75.0, 22.0], "quizzes": [0.0, 75.0, 78.0],  "tests": [100.0, 100.0] }
6a) Створити список ( students ), що містить lloyd, alice, tyler

6b) Для кожного студента надрукувати інформацію у читабельному форматі

6с) Напишіть функцію average ( Приймає список, вертає результат.
  Всередині функції викличіть вбудовану функцію sum() передавши аргумент.
   Результат помістити в змінну total. Привести total до типу float
    ( число з плаваючою точкою). Поділити total на кількість елементів
     у вхідному списку використавши len функцію. Вернути результат.

6d) Написати функцію get_letter_grade ( Використати if elif else.
 Якщо  90 і більше A, 70-90 B, 50-70 C, решта D. Функція примає число вертає Оцінку A, B, C або D.)

6e) перевірити функцію get_letter_grade.
 Знайти середню оцінку по домашніх завданнях для кожного студента і надрукувати.
  (Тобто спочатку викликати функцію average[‘homework’],
   і передати результат в функцію get_letter_grade)

6e) Знайти середню оцінку для всього класу. ( в числовому і буквенному виразі )
"""

import inflect

lloyd = {"name": "Lloyd", "homework": [90.0, 97.0, 75.0, 92.0], "quizzes": [88.0, 40.0, 94.0], "tests": [75.0, 90.0]}
alice = {"name": "Alice", "homework": [100.0, 92.0, 98.0, 100.0], "quizzes": [82.0, 83.0, 91.0], "tests": [89.0, 97.0]}
tyler = {"name": "Tyler", "homework": [0.0, 87.0, 75.0, 22.0], "quizzes": [0.0, 75.0, 78.0], "tests": [100.0, 100.0]}

# 6a
students = [lloyd, alice, tyler]
# 6b
for student in students:
    print(
        """Student: {},
     Grades: homework: {}, quizzes: {}, tests: {}""".format(
            student['name'], student['homework'], student['quizzes'], student['tests'])
    )
# wrapper
print()


# 6c
def average(data):
    total = sum(data)
    total = float(total) / len(data)
    return total


# 6d
def get_letter_grade(result):
    if result > 90:
        return "A"
        print("A")
    elif 70 <= result <= 90:
        return "B"
        print("B")
    elif 50 <= result < 70:
        return "C"
        print("C")
    else:
        return "D"
        print("D")


# 6e
for student in students:
    print("Student {}: Average grade: {}".format(
        student['name'], get_letter_grade(average(student['homework']))))


# 6d (Used inflect python package to convert numbers to words, https://pypi.org/project/inflect/)
# Example: Average grade for entire group is: 78.15, seventy-eight point one five, B.
av_total_grade = 0
engine = inflect.engine()

for student in students:
    per_student = student['homework'] + student['quizzes'] + student['tests']
    av_total_grade += average(per_student)
av_total_grade = round(av_total_grade / len(students), 2)

print("Average grade for entire group is: {}, {}, {}".format(
    av_total_grade, engine.number_to_words(av_total_grade), get_letter_grade(av_total_grade)))
