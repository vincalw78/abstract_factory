# -*- coding: utf-8 -*
# Завантажте текстову версію однієї з книг із сайту Project Gutenberg’s.
# Замініть усі розриви рядків у тексті символом пропуску
# і запишіть відформатований текст у новий файл formatted_text.txt.


book = './files/The_Haunted_Mind.txt'
new_file_book = './files/The_Haunted_Mind_formatted_version.txt'

# find maximum line length
# if the \n found before last char replace all whitespaces with underscore to the end of line.


def reader(file):
    max_length = find_max_length(file)
    with open(file, 'r') as f, open(new_file_book, 'w') as new_f:
        for line in f.readlines():
            for index, char in enumerate(line):
                if char == '\n' and index != max_length:
                    line = replacer(line, char)
                    line = line + '_' * (max_length - index)
                    print(line)
            new_f.writelines(line + '\n')


def find_max_length(file):
    max_length = []
    with open(file, 'r') as f:
        for line in f.readlines():
            max_length.append(len(line))
    return max(max_length)


def replacer(line, char):
    return line.replace(char, '_')


if __name__ == '__main__':
    print(reader(book))
