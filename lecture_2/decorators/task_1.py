# Напишіть декоратор ( функцію logg), яка обертає функції.
#  Суть декоратора  в тому, що він логує (записує у файл) позиційні і ключова аргументи.
#  В кінці враппера записати у файл ‘Arguments are written\n’.
#  Також створити дві функції add & multiply, які підповідно додають,
#  перемножують позиційні аргументи і вертають результат.
#  Обернути функції add & multiply декоратором logg і викликати їх
#  через if __name__ == “__main__”. Перевірити лог файл чи декоратор спрацював.
from functools import reduce
import os


# decorator
def logg(func):
    def wrapper(*args):
        with open('../../args.txt', 'a+') as f:
            f.write('The following args of func: {}, have been passed: \n'.format(func.__name__))
            for item in args:
                f.write(str(item) + ' ')
            f.write('Arguments are written\n')
            return func(*args)
    return wrapper


@logg
def add(*args):
    return sum(args)


@logg
def multiply(*args):
    return reduce(lambda x, y: x * y, args)


if __name__ == '__main__':
    print(add(1, 5, 10))
    print(multiply(1, 5, 20))
    decision = input("remove fail after test?: ")
    if decision == 'yes':
        os.remove('../../args.txt')
