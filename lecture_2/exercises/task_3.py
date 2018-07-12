# Написати функцію( gen_random) яка генерує рандомне число від 1 до 10.
#  Якщо число = 1, то вернути його, якщо більше 1 то викликати помилку (ImportError).
#  Написати функцію run ( яка буде викликати функцію gen_random і друкувати результат.
#  Створити декоратор retry, який буде 20 разів пробувати викликати функцію gen_random.
#  Якщо за 20 разів gen_random не вернув результат то вернути ‘NO RESULT’.
#  Запустити програму.
import random


def retry(*dec_args, **dec_kwargs):

    def real_decorator(func):
        def wrapper():
            print(dec_args)
            for attempt in range(dec_args[0]):
                print('attempt {}'.format(attempt+1))
                try:
                    res = func()
                except ImportError as err:
                    continue
                else:
                    return res
            return 'NO RESULT'
        return wrapper
    return real_decorator


@retry(20)
def gen_random():
    num = random.randint(1, 10)
    if num == 1:
        return num
    raise ImportError("{} number has been generated...".format(num))


def run():
    print(gen_random())


if __name__ == '__main__':
    run()
