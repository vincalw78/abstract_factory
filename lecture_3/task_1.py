# Написати функцію, яка створить  файл numbers.txt,
#  якщо його не існує.  Запишіть у файл 10 чисел,
#  кожне з нового рядка ( згенерувати модулем random від 1 до 100).
#  Напишіть функцію, яка зчитує ці числа з файлу і обчислює їх суму,
#  виводить цю суму на екран і, водночас,
#  записує цю суму у інший файл під назвою sum_numbers.txt
import random
import os


def task1():
    with open('./files/numbers.txt', 'x') as fi:
        for x in range(10):
            fi.writelines(str(random.randint(1, 100)) + '\n')


def task_read():
    with open ('./files/numbers.txt', 'r') as fi, open('./files/sum_numbers.txt', 'w') as fi2:
        result = fi.readlines()
        result_int = list(map(lambda x: int(x), result))
        fi2.write(str(sum(result_int)))
    return sum(result_int)



task1()
print(task_read())

os.remove('./files/numbers.txt')
#os.remove('sum_numbers.txt')
