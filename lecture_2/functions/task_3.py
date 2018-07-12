# Написати функцію, яка випадковим чином вертає число у проміжку від 0 до 10.
#  ( random_10) Відповідно Написати функцію (summarizer). Яка містить змінну result=0.
#   Функція summarizer викликає функцію random_10
#  і додає до суми рузультат. Якщо результат більше 100 то надрукуйте результат.

import random


def random_10():
    return random.randint(0, 10)


def summarizer():
    result = 0
    while not result > 100:
        result += random_10()
    else:
        print(result)
        return True


if __name__ == '__main__':
    summarizer()


