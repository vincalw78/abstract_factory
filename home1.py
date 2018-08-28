from decimal import *


def main():
    num_of_st = input('Enter stud number: ')

    stud_marks = dict()
    for x in range(int(num_of_st)):
        stud_info = input('Enter stud marks: ').split()
        stud_marks[stud_info[0]] = stud_info[1:]

    target_name = input('Enter stud name: ')
    # import ipdb; ipdb.set_trace()
    result = sum(Decimal(x) for x in stud_marks[target_name]) / 3
    print(result.quantize(Decimal('0.01')))


if __name__ == '__main__':
    main()
