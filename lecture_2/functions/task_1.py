# Напишіть функцію max_of_three, яка приймає три числа і вертає максимальне із них.
# Викликати функцію і надрукувати результат.


def max_of_three(one, two, three):
    try:
        result = [float(num) for num in [one, two, three]]
    except ValueError as err:
        print('Must be a number: {}'.format(err))
        return False

    print(max(result))


if __name__ == '__main__':
    max_of_three(1100122, 22, 33)
    max_of_three('1000', 19, 1.3)
    max_of_three('sda', 123, 100)

