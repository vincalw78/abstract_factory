from user import User


class Admin(User):
    privileges = ('create_role', 'delete_role')

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.priv = Privileges()


class Privileges:

    def __init__(self):
        self.privileges = Admin.privileges

    def show_privileges(self):
        print(self.privileges)


if __name__ == '__main__':
    admin_user = Admin('Super', 'Duper')
    admin_user.priv.show_privileges()
