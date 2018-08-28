from collections import deque


def main():
    dec = deque()

    n = int(input('Num of operations'))

    for _ in range(n):
        op = input().split()
        getattr(dec, op.pop(0))(*[int(x) for x in op])

    print(' '.join([str(x) for x in dec]))


if __name__ == '__main__':
    main()
