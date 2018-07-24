# a:
# Створіть класс з імям Shop(), метод ініт повинен містити два атрибути:
# shop_name, store_type

# Створіть метод describe_shop() який виводить два атрибути
# і метод open_shop() який виводить повідомлення про те що онлайн магазин відкритий

# Створіть на основі класу екземпляр з імям store, виведіть два атрибути окремо потім
# викличте два методи

# ----
# b: створіть три різні екзепляри, викличіть метод describe_shop для кожного.
# ----

# c:
# додайте атрибут number_of_units, зі значенням по замовчуанню 0.
# він представляє кіклькість видів товару в магазині.
# створіть екземпляр з імям store, виведіть number_of_units а потім змініть значення і виведіть знову
# ----

# d:
# Додайте метод з імям set_number_of_units(), що дозволяє задати кількість видів товару
# Викличте метод з новим числом знову виведіть значення.
# Додайте метод increment_number_of_units() який збільшує кількітсь видів товару на задану велечину,
# викличте цей метод

# e:
# Напишіть клас Discount() що успадковується від Shop()
# Додайте атрибут з імям discount_products для зберігання списку товарів на які встановленя знижка
# Напишіть метод get_discounts_products() який виводить цей список
# Створіть екземпляр store_discount і викличте цей метод

# f:
# збережіть код класу у Shop() модулі створіть окремий файл зо імпортує класс Shop()
# створіть екземпляр all_store і викличте один з методів Shop() щоб перевірити що команда імпорт працює вірно
from shop import Shop


class Discount(Shop):

    def __init__(self, shop_name, store_type, discount_products):
        super().__init__(shop_name, store_type,)
        self.discount_products = discount_products

    def get_discounts_products(self):
        print(self.discount_products)


if __name__ == '__main__':
    # a
    print('a task')
    store = Shop('Golden Car', 'used cars trade in')
    print(store.shop_name)
    print(store.store_type)
    store.describe_shop()
    store.open_shop()

    # b створіть три різні екзепляри, викличіть метод describe_shop для кожного
    print('b task')
    store1 = Shop('shop1', 'trading1')
    store2 = Shop('shop2', 'trading2')
    store3 = Shop('shop3', 'trading3')
    for st in store1, store2, store3:
        st.describe_shop()

    # c
    print('c task')
    store = Shop('shop form task c', 'trading c')
    print(store.number_of_units)
    store.number_of_units = 5
    print(store.number_of_units)

    # d
    print('d task')
    store.set_number_of_units(10)
    print(store.number_of_units)
    store.increment_number_of_units(15)
    print(store.number_of_units)

    # e
    store_discount = Discount('Shop D', 'trading D', ['audi', 'reno'])
    store_discount.get_discounts_products()

    # f
    all_store = Shop('shop F', 'trading F')
    all_store.open_shop()
