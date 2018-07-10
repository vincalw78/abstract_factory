"""
1)  Створіть англо-німецький словник, який називається e2g,
     і виведіть його на екран. Слова для словника:
     stork / storch, hawk / falke, woodpecker / specht і owl / eule.

2)  Виведіть німецький варіант слова owl.

3)  Додайте у словник, на ваш вибір, ще два слова та їхній переклад.

4)  Виведіть окремо:
     словник; ключі і значення словника у вигляді списків.
"""

# 1
e2g = {
    'stork': 'storch',
    'hawk': 'falke',
    'woodpecker': 'specht',
    'owl': 'eule'
}

# 2
print('Printing translated version of the word owl:')
print(e2g['owl'])
print()

# 3
e2g['river'] = 'fluss'
e2g['donut'] = 'crapfen'

# 4
print('Printing e2g dictionary:')
print(e2g)
print()

print('Printing keys and values as dict:')
print([k for k in e2g])
print([v for _, v in e2g.items()])
print()
