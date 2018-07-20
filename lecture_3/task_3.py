# Функція replace() може використовуватися для заміни будь-якого слова у рядку іншим словом.
# Прочитайте кожен рядок зі створеного у попередньому завданні файлу learning_python.txt
# і замініть слово Python назвою іншої мови, наприклад C при виведенні на екран.
# Це завдання написати в окремій функції.


def text_reader():
    with open('./files/learning_python.txt', 'r') as f:
        for index, line in enumerate(f.readlines()):
            print(index+1, ruby_replacer(line), sep='. ')


def ruby_replacer(text_line):
    return text_line.replace('Python', 'Ruby')


if __name__ == '__main__':
    text_reader()
