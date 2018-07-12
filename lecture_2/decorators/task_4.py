# Написати 2 функції add ( додає позиційні аргументи в циклі for і вертає результат)
# і add_advance( яка додає позиційні аргументи використовуючи builtin функцію sum).
#  Написати декоратор deprecated_add, обгорнути функцію add.
#  У враппері натомість викликати функцію add_advanced замість add,
#  і друкувати користувачеві повідомлення, що add функція є deprecated.
#  Перевірити чи дійсно викликається функція add_advance.
#  (Удосканалити depracated _add від певної дати переданої декоратору в аргумент )
import datetime


def deprecated_add(*args, **kwargs):
    if kwargs['year'] and kwargs['month'] and kwargs['day']:
        started_date = datetime.date(kwargs['year'], kwargs['month'], kwargs['day'])
    else:
        raise KeyError("Please set date which add method considered as deprecated from")

    def dep_wrapper(func):
        def wrapper(*args, **kwargs):
            if started_date < datetime.date.today():
                print(f'{func.__name__} is deprecated use add_advance instead')
                return add_advance(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return dep_wrapper


@deprecated_add(year=2018, month=3, day=13)
def add(*args, **kwargs):
    print('Add is called')
    res = 0
    for x in args:
        res += x
    return res


def add_advance(*args, **kwargs):
    print('Add advance is called')
    return sum(args)


if __name__ == '__main__':
    print(add(1, 3, 5))
