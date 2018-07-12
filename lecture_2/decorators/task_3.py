# Удосконалити декоратор із 2 завдання, щоб було можливість передати декоратору ключовий
#  аргумент наприклад time_caching=60,  і відповідно перевіряти чи дані
#  є давнішими ніж time_caching, якщо давнішими наново виконати функцію add.

import datetime
import time


cached_info = {}


def cached(**deco_kwargs):

    def deco_wrapper(func):
        def wrapper(*args):
            if args in cached_info:
                t_diff = (datetime.datetime.now() - cached_info[args]['date_accessed']).seconds
                if t_diff > deco_kwargs['time_caching']:

                    # rewriting cache
                    time.sleep(2)

                    print('Rewriting cache... last access was {} seconds ago'.format(t_diff))
                    cached_info[args] = {'date_accessed': datetime.datetime.now(),
                                         'value': func(*args)}
                else:
                    print('returning cached result...')
                    return cached_info[args]

            print(f'returning {func.__name__} function...')
            cached_info[args] = {'date_accessed': datetime.datetime.now(),
                           'value': func(*args)}
            return cached_info[args]
        return wrapper
    return deco_wrapper


@cached(time_caching=60)
def add(*args):
    # accessing function
    time.sleep(2)

    return sum(args)


if __name__ == '__main__':
    print(add(123))
    print(add(123))

    # rewriting cache, time delta should be > 60s
    time.sleep(70)
    print(add(123))


