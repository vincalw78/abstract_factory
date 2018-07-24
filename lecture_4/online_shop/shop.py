class Shop:

    # a
    def __init__(self, shop_name, store_type, number_of_units=0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units

    def describe_shop(self):
        print('name: {}, type: {}'.format(self.shop_name, self.store_type))

    def open_shop(self):
        print('The shop {} has been opened'.format(self.shop_name))

    def set_number_of_units(self, number_of_units):
        self.number_of_units = number_of_units

    def increment_number_of_units(self, increment):
        self.number_of_units += increment
