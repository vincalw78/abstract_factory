# Напишіть функцію, яка приймає рядок як параметр і повертає True,
# якщо рядок є паліндром, інакше False.
# Паліндром ( слово читається однаково ззаду-наперед,
# var == var[::-1], var -> паліндром ( використати рекурсію)


def palindrom_checker(line):
    line = line.lower().replace(" ", "")
    if line == (line[::-1]):
        return True
    return False


if __name__ == '__main__':
    print(palindrom_checker(input('Please enter a line to check whether it is palindrom: ')))