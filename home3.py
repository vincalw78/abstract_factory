from decimal import *
from collections import namedtuple


def main():

    n = int(input('Num of stud'))
    headers = input()
    Student = namedtuple('Student', headers)
    sum_marks = Decimal(0)

    for x in range(n):
        stud = Student(*(input().split()))
        sum_marks += Decimal(stud.MARKS)

    result = sum_marks / n

    print(result.quantize(Decimal('0.01')))


if __name__ == '__main__':
    main()
