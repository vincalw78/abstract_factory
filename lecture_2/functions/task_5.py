# Написати функцію (len_of_args), яка приймає ключові та позиційні аргументи
#  ( вертає довжину позиційних елементів - len(args) ) .
#  Також  написати функцію rand_of_el, яка двічі викликає функцію len_of_args
#  і вертає різницю результатів.  Викликати функцію rand_of_el і надрукувати результат.


def len_of_args(*args, **kwargs):
    return len(args)


def rand_of_el():
    return len_of_args() - len_of_args()


print(rand_of_el())
