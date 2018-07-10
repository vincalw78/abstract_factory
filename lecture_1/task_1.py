"""
На вхід програми подається один рядок з цілими числами.
 Числа розділені пропусками. Необхідно вивести суму цих чисел.
  Наприклад, якщо був введений рядок чисел 2 -1 9 6,
   то результатом роботи програми буде їх сума 16.
    Написати 2 функції( 1 функція приймає інпут від юзера,
     і передає агрумент 2 функції яка робить обчислення і виводить результат)
"""


def printer():
    """takes input and prints output"""
    data = input("Please enter a list of numbers separated by whitespace char: ")
    print(_calculator(data))


def _calculator(numbers):
    """calculate sum of passed numbers"""
    numbers = [int(number) for number in numbers.split()]
    return sum(numbers)


if __name__ == '__main__':
    printer()
