# Напишіть функцію, яка генерує словник.
#  Де ключами є слова square, cubic, four, five.
#  А значення будуть лямбда функції які приймають число як аргумент,
#  а вертають піднесення до відповідного степеня.
#  У функції по черзі викликати лямбда функції із випадково згенерованим числом від 10 до 20.
import random


def figure_generator():
    func = lambda x: x**2
    data = {
        'square': func,
        'cubic': func,
        'four': func,
        'five': func
    }
    for key in data:
        print(data[key](random.randint(10, 20)))


if __name__ == '__main__':
    figure_generator()
