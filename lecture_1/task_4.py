"""
Є словник (продовження на наст слайді):  inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

Спробуйте зробити наступне:
     4a)    Додайте ключ до словника під назвою "pocket".

     4b)    Встановіть значення "pocket" як список, що складається з рядків
      'seashell', 'strange berry', і  'lint’

     4с)    Відсортуйте ( .sort ()) елементи зі списку,
      що зберігаються під ключем  "backpack". ( і надрукуйте)

     4d)    Потім видаліть ("dagger") зі списку предметів,
      що зберігаються під ключем “backpack".

     4e)    Додайте 50 до числа, збереженого під "gold" ключем. І надрукуйте результат.
"""

inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# 4a
print('Adding key: "pocket"... \n')
inventory['pocket'] = ''

# 4b
print('Adding a list to the "pocket" key... \n')
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# 4c
print('Printing sorted version of "backpack key":')
inventory['backpack'].sort()
print(inventory['backpack'])
print()

# 4d
print('Removing dagger from backpack...')
inventory['backpack'].remove('dagger')
print(inventory['backpack'])
print()

# 4e
print('Adding 50 gold...')
inventory['gold'] = inventory['gold'] + 50
print(inventory['gold'])
