# Написати функцію random_from_list, яка приймає список слів,
#  і вертає те слово, яке є найдовшим.
from functools import reduce

words_list = ["shark", "cow", "hedgehog"]


def random_from_list(words):
    print(reduce(lambda x, y: x if len(x) > len(y) else y, words))


if __name__ == '__main__':
    random_from_list(words_list)
