"""
    5a) Створіть новий словник під назвою prices за допомогою {}

    5b) Покладіть в словник такі значення
     "banana": 4, "apple": 2, "orange": 1.5, "pear": 3

    5с) Створити новий словник stocks.
    ( який буде містити інформацію для кожного ключа із prices скільки товару
     ( запасу є на складі). Згенерувати значення випадковим чином.

    5d) Проітеруйтесь в циклі  через кожен  ключ  в prices.
     Для кожного ключа надрукуйте ключ разом із ціною, а також запасом на складі.
      Надрукуйте відповідь у наступному форматі:
apple
price: 2
stock: 5

   5e) Давайте визначимо, скільки грошей ви зробили б,
    якщо б ви продали всю їжу ( змінна total, треба вирахувати і надрукувати її )
"""
import random

# 5a 5b 5c
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
stocks = dict()
for key in prices:
    stocks[key] = random.randint(1, 10)
print(stocks)
# wrapper
print()

# 5d
for k1, k2 in zip(prices, stocks):
    print('{}: {}, available in stock: {}'.format(k1, prices[k1], stocks[k2]))
# wrapper
print()

# 5e
total = 0
for k1, k2 in zip(prices, stocks):
    total += (prices[k1] * stocks[k2])
print("Total amount of money in a case all goods are sold")
print(total)
