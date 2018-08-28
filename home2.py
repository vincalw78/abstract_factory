from datetime import datetime


def main():
    n = input("num of posts")
    result = []
    for x in range(int(n)):
        date1 = input()
        first_date = datetime.strptime(date1, '%a %d %b %Y %H:%M:%S %z')

        date2 = input()
        second_date = datetime.strptime(date2, '%a %d %b %Y %H:%M:%S %z')
        delta = abs((first_date - second_date).total_seconds())
        result.append(int(delta))
        print('='*60)

    print(result)


if __name__ == '__main__':
    main()
