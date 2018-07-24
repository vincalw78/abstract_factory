# Облік користувачів на сайті.


class User:

    def __init__(self, first_name, *last_name, login_attempts=0):
        self.first_name = first_name
        self.login_attempts = login_attempts
        self.last_name = last_name

    def describe(self):
        last_name = ''
        for index, _ in enumerate(self.last_name):
            last_name += ' ' + self.last_name[index] + ' '

        full_name = self.first_name + last_name
        print(full_name)
        return full_name

    def greeting_user(self):
        print('Greeting! {}'.format(self.describe()))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


if __name__ == '__main__':
    print()
    # user1 = User('Oleg', 'Stivensonn')
    # user2 = User('Ryan', 'Giggs')
    # user3 = User('Paul', 'Scholes')
    #
    # for user in user1, user2, user3:
    #     user.greeting_user()
    #
    # user4 = User('John', 'Banderlou')
    # user4.increment_login_attempts()
    # user4.increment_login_attempts()
    # print(user4.login_attempts)
    # user4.reset_login_attempts()
    # print(user4.login_attempts)

    admin_user = Admin('Super', 'Duper')
    admin_user.priv.show_privileges()









