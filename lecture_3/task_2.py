# Створіть новий файл у текстовому редакторі і напишіть 3 рядки тексту у ньому про можливості Python.
# Кожен рядок повинен починатися з фрази: In Python you can ....
# Збережіть файл під ім’ям learning_python.txt. Напишіть функцію,
# яка зчитує файл і виводить текст з перебором рядків об’єкта файлу
#  і зі збереженням рядків у списку з подальшим виведенням списку поза блоком with


def text_parser():
    with open('./files/learning_python.txt', 'r+') as f:
        text_copy = f.readlines()
        f.seek(0)
        for num, line in enumerate(f.readlines()):
            print(num+1, line, sep='. ')
        return text_copy


if __name__ == '__main__':
    text_in_list = text_parser()
    print('_______')
    print('The following list can be used afterwards:')
    print(text_in_list)

