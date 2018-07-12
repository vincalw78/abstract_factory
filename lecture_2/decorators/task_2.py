# Скопіювати функцію add із попереднього прикладу.
#  Написати декоратор cached. Суть декоратора в кешуванні роботи функції add.
#  Тобто треба створити словник де ключами будуть аргументи ( позиційні )
#  а значенням буде результат виконання функції add.
#  Відповідно декоратор має перевіряти чи є
#  дані в словнику(була вже викликана функція add із такими аргументами)
#  і вернути результат. Програмно перевірити чи дані беруться із кешу чи виконується функція add?
import timeit
import time

cached_info = {}


def cached(func):
    def wrapper(*args):
        if args in cached_info:
            print('returning cached result...')
            return cached_info[args]

        print(f'returning {func.__name__} function...')
        cached_info[args] = func(*args)
        return cached_info[args]

    return wrapper


@cached
def add(*args):
    time.sleep(5)
    return sum(args)


if __name__ == '__main__':
    print(timeit.timeit('add(123)', setup='from __main__ import add', number=1))
    print(timeit.timeit('add(123)', setup='from __main__ import add', number=1))
    print(timeit.timeit('add(123)', setup='from __main__ import add', number=1))
