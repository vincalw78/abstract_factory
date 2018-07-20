# -*- coding: utf-8 -*
# Завантажте текстову версію книги The Life and Adventures of Robinson Crusoe By Daniel Defoe
# із сайту Project Gutenberg’s. Витягніть із тексту заголовки усіх розділів,
# які мають вигляд, на зразок: CHAPTER I—START IN LIFE.
# Запишіть знайдені назви у новий файл chapters.txt

book = './files/robinson.txt'
chap = './files/chapters.txt'


def reader():
    with open(book, 'r', encoding="utf-8") as book_f, open(chap, 'w', encoding="utf-8") as chap_f:
        for line in book_f.readlines():
            if 'CHAPTER' in line:
                chap_f.writelines(line)


if __name__ == '__main__':
    reader()
