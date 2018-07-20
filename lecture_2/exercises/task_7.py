# Написати timing декоратор. Суть якого виміряти час виконання функції.
# І після виконання декорованої функції надрукувати час. Написати функцію test_list_long
# ( ця функція  приймає аргумен n, і в циклі for послідовно додає числа від 1 до n до нашого списку)
# Функція test_list_long  нічого не вертає.
# Написати функцію test_list_advance ( приймає аргумент n і створює список довжиною n )
# li = [True]*n  .   В циклі for послідовно змінювати кожен елемент списку на значення від 1 до n.
# Ця функція теж нічого не вертає. В теорії функція test_list_advance  має працювати швидше
# оскільки С-масиви не будуть перекопійовуватись.
# Задекорувати створені функції timing декоратором і викликати із аргументом 10**12.
import timeit


# decorator, time execution measurement
def timing():
    pass


def t_list_long(n):
    li = []

    for num in range(n):
        li.append(num+1)


def t_list_advance(n):
    li = [True]*n

    for index, _ in enumerate(li):
        li[index] = index+1


if __name__ == '__main__':
    print(timeit.timeit('t_list_long(10**6)', setup='from __main__ import t_list_long', number=1))
    print(timeit.timeit('t_list_advance(10**6)', setup='from __main__ import t_list_advance', number=1))
