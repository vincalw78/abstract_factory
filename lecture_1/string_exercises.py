"""
Вправи строки (кожне завдання в окремій функції всі завдання в  1 файлі)

1. Напишіть код, який приймає рядок як вхідний і повертає рядок задом наперед.

2. Юзер вводить строку. (наприклад  inp = ‘saveChangesInTheEditor’).
 Вивести на екран скільки слів є цьому інпуті.
  ( враховувати що нове слово починається із великої літери)

3. pangram - строка яка містись усі літери англійської абетки.
 Перевірити чи введена строка є pangram

4. Є строка S, ми можемо перетворити кожну букву окремо на малу або велику, щоб створити іншу строку. Треба вернути список всіх можливих комбінацій. Наприклад є строка var = ‘it’ результатом буде result_list = [‘IT’, “It”, “iT”, ‘it’].

5. (hackerrank) Юзер вводить строку. Перевірити чи ця строка є послідовністю цифр. Тобто
         var = ‘91011’  є послідовністю, треба надрукувати ‘YES’.
         var = ‘10001003’ не є послідовністю, треба надрукувати ‘NO’

6. (hackerrank) Юзер вводить пароль. Вивести на екран кількість символів, яких не вистачає щоб цей пароль був “складним”. Для того щоб пароль був складним потрібно, щоб пароль складався як мінімум із 6 символів, містив у собі по одному символу із вказаних наборів:
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

"""

import string
import itertools
import re


# 1
def reverse(line):
    return line[::-1]


# 2
counter = 0
input_text1 = "someWordInHere"
input_text2 = "word"
input_text3 = ""

inputs = [input_text1, input_text2, input_text3]


def count_words(line):
    global counter
    if line:
        counter = 1
        for char in line:
            if char in string.ascii_uppercase:
                counter += 1
        print(counter)
    else:
        print('There is no word inside')


[count_words(text) for text in inputs]
# wrapper
print()

# 3
i_am_pangram = "Waltz, nymph, for quick jigs vex bud."
i_am_a_famous_string = "Hello World"

inputs = [i_am_pangram, i_am_a_famous_string]


def pangram_detector(line):
    for char in string.ascii_lowercase:
        if char not in line:
            return False
        return True


[print(pangram_detector(sentence)) for sentence in inputs]


# 4
inp = 'CBS'


def possible_varians(line):
    iter_res = map(''.join, itertools.product(*zip(line.upper(), line.lower())))
    res = [res for res in iter_res]
    print(res)


possible_varians(inp)


# 5 ???

# 6
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"


def password_check(password):
    """
    Verify the strength of 'password'
    Returns a dict indicating the wrong criteria
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """

    # calculating the length
    length_error = len(password) < 6

    # searching for digits
    digit_error = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None

    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # searching for symbols
    symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None

    # overall result
    password_ok = not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error)

    return {
        'password_ok' : password_ok,
        'length_error' : length_error,
        'digit_error' : digit_error,
        'uppercase_error' : uppercase_error,
        'lowercase_error' : lowercase_error,
        'symbol_error' : symbol_error,
    }


if __name__ == '__main__':
    print(password_check(input("Please enter password: \n")))
