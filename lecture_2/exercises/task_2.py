# Написати функцію, яка генерує ( рандомно)
#  список списків( 5 вкладених списків ) довжиною 5 елементів.
#  Відсортувати 1 список по 4 елементу вкладених списків.
#  Вивести відсортований список на екран.
import random


def randomizer():
    parent = []
    for _ in range(5):
        child = random.sample(range(50), 5)
        parent.append(child)

    # before sorting
    print(parent)
    parent.sort(key=lambda x: x[3])
    # after sorting
    print(parent)


if __name__ == '__main__':
    randomizer()
