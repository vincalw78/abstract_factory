"""
Cтворіть словник з трьома річками і регіонами, територією яких вони протікають.
 Одна з можливих пар «ключ: значення» - 'Amazon': 'South America'.
  Додайте ще дві пари «річка: регіон» у словник.
   Виведіть повідомлення із назвами річки і регіону - наприклад,
    «The Amazon runs through South America.» для усіх елементів словника,
     враховуючи те, що у повідомлення у відповідні місця
      підставляються назви річок і територій.
       ( використати створення функції і метод format )

"""

RIVERS = {
    'Amazon': 'South America',
    'Dnipro': 'Ukraine',
    'Thames': 'United Kingdom'
}


def pretty_output(data):
    """format output"""
    for river, region in data.items():
        print("The {} runs through {}.".format(river, region))


if __name__ == '__main__':
    pretty_output(RIVERS)
