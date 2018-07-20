# До попередньої задачі. Визначте відсоток малих і великих літер у тексті,
# що зберігається у файлі.
# Скористайтеся, як зразком вхідного файлу,
# текстовий файл із сайту Project Gutenberg’s. Використайте функцію isalpha()

book = './files/robinson.txt'
upper = []
lower = []


def register_case_counter():
    with open(book, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            for char in line:
                if char == char.upper() and char.isalpha():
                    upper.append(char)
                elif char == char.lower() and char.isalpha():
                    lower.append(char)
    low_chars = len(lower)
    upp_chars = len(upper)

    print('lower case percentage is {}'.format(round(low_chars / (low_chars + upp_chars), 2)))
    print('upper case percentage is {}'.format(round(upp_chars / (low_chars + upp_chars), 2)))


if __name__ == '__main__':
    register_case_counter()
