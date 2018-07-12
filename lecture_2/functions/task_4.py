# Написати функцію ( find_super ). Функція приймає на вхід число.
#  А повинна вернути суму цифр вхідного числа ( якщо ця сума менша 10).
#  Тобто якщо вхідне число = 12345. То сума цифр = 15 ( 15 > 10 ),
#  тобто треба вернути суму цифр  вже 15. (застосувати рекурсію)

"""
fact(5)
| 5  * fact(4)
|| 5 * (4 * fact(3))
||| 5 * (4 * (3 * fact(2))
|||| 5 * (4 * (3 * (2 * fact(1))))
||||| 5 * (4 * (3 * (2 * (1 * fact(0)))))
|||||| 5 * 4 * 3 * 2 * 1 * 1
120
"""


def find_super(n):
    print("Calling inside <<FUNC>>")
    # basic condition, will be called in the end once
    if len(n) == 1:
        print("Calling inside <<IF>>")
        return n[0]
    else:
        print("Calling inside <<ELSE>>")
        return n[0] + find_super(n[1:])  # looping


if __name__ == '__main__':
    print(find_super([1, 2, 3, 4, 5]))  # 1 + ( 2 + ( 3 + ( 4 + (5))))
