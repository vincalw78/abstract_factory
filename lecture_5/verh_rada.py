# -*- coding: cp1251 -*-
import pickle
import pdb


# pickle db file
db_file = './db_data/vr_db.pickle'


# Base class
class Human:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def __eq__(self, other):
        return self.weight == other.weight and \
               self.height == other.height

    def __hash__(self):
        return hash(self.weight) + hash(self.height)

    def __str__(self):
        return f'Human with: weight: {self.weight} height: {self.height}'


# Deputies hashed
class Deputat(Human):
    def __init__(self, weight, height, last_name, first_name, age, bribe_taker):
        super(Deputat, self).__init__(weight, height)
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.bribe_taker = bool(int(bribe_taker))
        self.bribe_amount = 0

    def __eq__(self, other):
        return self.weight == other.weight and \
               self.height == other.height and \
               self.age == other.age

    def __hash__(self):
        return hash(self.weight) + hash(self.height) + hash(self.age)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.weight}kg {self.height}cm {self.age}age'

    @staticmethod
    def describe_deputy():
        personal_data = input(
            'Please enter: weight, height, last_name, first_name, age, is_briber?[0 or 1]: '
        )

        pd = personal_data.split(', ')

        # should work fine if Deputat class is hashed. expected equal() to return True.
        try:
            deputy = Deputat(pd[0], pd[1], pd[2], pd[3], pd[4], pd[5])
            return deputy
        except IndexError as err:
            print('data should be separated by comma and whitespace', 'Invalid Data')

    def give_tribute(self):
        if self.bribe_taker is False:
            print('this deputy does not take bribes...')
            return False

        money = input('how much grivnjas would you like to give:')
        if int(money) > 10000:
            print('Police will arrest the deputy!')
            return False

        self.bribe_amount += int(money)
        return self.bribe_amount


# Functor sorts deputies by params
class Sorting:
    def __init__(self, *args):
        self.args = args

    def __call__(self, instance):
        values = []
        for value in self.args:
            values.append(getattr(instance, value))
        return values


# Fraction contains deputy members
class Fraction:
    def __init__(self, name):
        self.name = name
        self.deputies = []

    def __str__(self):
        return f'{self.name} members: {len(self.deputies)}'

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def add_deputy(self):
        deputy = Deputat.describe_deputy()

        if not deputy:
            print('please describe deputy correctly, Invalid Data')
            return False

        if deputy not in self.deputies:
            self.deputies.append(deputy)
            print(f'{deputy} has been added to the fraction; {self.name}')
            return deputy
        else:
            print(f'{deputy} is already a participant of the fraction {self.name}')

    def remove_deputy(self, deputy=None):
        if not deputy:
            personal_data = input(
                'Please enter: weight, height, last_name, first_name, age, is_briber?[True or False]: '
            )
            pd = personal_data.split(', ')

            # should work fine if Deputat class is hashed. expected equal() to return True.
            try:
                deputy = Deputat(pd[0], pd[1], pd[2], pd[3], pd[4], bool(pd[5]))
            except IndexError as err:
                print('data should be separated by comma and whitespace', 'Invalid Data')
                return False

        if deputy in self.deputies:
            self.deputies.remove(deputy)
            print(f'{deputy} has been excluded from the fraction: {self.name}')
        else:
            print(f'{deputy} is not a participant of the fraction: {self.name}')

    def find_all_deputies(self):
        deputies = list(self.deputies)
        deputies.sort(key=Sorting('first_name', 'last_name'))

        print('List of all deputies...')
        for deputy in deputies:
            print(deputy)

    def find_all_bribe_takers(self):
        print('The following bribe_takers have been found...')
        deputies = [dep for dep in self.deputies if dep.bribe_taker]
        deputies.sort(key=Sorting('bribe_amount'))

        for deputy in deputies:
            print(deputy, 'grivnjas taken: {}'.format(deputy.bribe_amount))

    def find_highest_bribe_taker(self):
        print('The most greedy deputy is:')
        deputies = [dep for dep in self.deputies if dep.bribe_taker]
        deputies.sort(key=Sorting('bribe_amount'))

        print(deputies[-1], 'grivnjas taken: {}'.format(deputies[-1].bribe_amount))

    def clean_out_deputies(self):
        print('All deputies has been cleaned out')
        self.deputies = []

    def is_participant(self, deputy, vr):
        for fraction in vr.fractions:
            if deputy in fraction.deputies:
                print(f'{deputy} is a member of the {self.name} fraction')
                return True

        print(f'{deputy} is not a member of the {self.name} fraction')
        return False


# Contains fractions can also add a deputy to a fraction or remove a deputy(remove from fraction.)
class VerkhovnaRada:
    def __init__(self):
        self.name = 'Verkhovna Rada Ukraine'
        self.fractions = []

    def add_fraction(self, fraction):
        if fraction not in self.fractions and fraction.name:
            print(f'Fraction {fraction.name} has been added to VR')
            self.fractions.append(fraction)
            return True

        print('already in VR')
        for index, fr in enumerate(self.fractions):
            if fr == fraction:
                fr.deputies += fraction.deputies
                self.fractions[index] = fr

    def remove_fraction(self, fraction):
        if fraction in self.fractions:
            print(f'Fraction {fraction.name} has been removed from VR')
            self.fractions.remove(fraction)
            return True

        print(f'Fraction {fraction.name} not in the list.')
        return False

    def print_all_fractions(self):
        print('List of all fractions:')
        for fr in self.fractions:
            print(fr)

    @staticmethod
    def print_fraction(fraction):
        print(fraction)

    @staticmethod
    def add_deputy_to_fraction(deputy, fraction):
        print(f'Adding deputy: {deputy} ...')
        fraction.add_deputy(deputy)

    def remove_deputy_from_fraction(self, deputy, fraction):
        print(f'Removing deputy: {deputy} ...')
        for fr in self.fractions:
            if fr == fraction:
                fr.remove_deputy(deputy)

    def print_all_bribe_takers(self):
        print('Printing all bribe takers in VR')
        for fraction in self.fractions:
            for deputy in fraction.deputies:
                if deputy.bribe_taker:
                    print(deputy, 'grivnjas taken: {}'.format(deputy.bribe_amount))

    def higher_bribe_taker(self):
        bribe_takers = []
        for fraction in self.fractions:
            for deputy in fraction.deputies:
                if deputy.bribe_taker:
                    bribe_takers.append(deputy)

        pdb.set_trace()
        bribe_takers.sort(key=Sorting('bribe_amount'))
        print(bribe_takers[-1], 'grivnjas taken: {}'.format(bribe_takers[-1].bribe_amount))

    def print_all_deputies(self):
        for fraction in self.fractions:
            print('{}: '.format(fraction.name))
            for deputy in fraction.deputies:
                print(''.rjust(len(fraction.name)), deputy)

    def is_present_in_vr(self, deputy):
        deputies = []
        for fraction in self.fractions:
            for dep in fraction.deputies:
                deputies.append(dep)

        print(deputy in deputies)

    def update_deputy(self, deputy):
        for fraction in self.fractions:
            for dp in fraction.deputies:
                if deputy == dp:
                    dp.bribe_amount = deputy.bribe_amount


class VerkhovnaRadaDataBase:
    @staticmethod
    def save_to_db(vr):
        confirmance = input('Are you sure? press yes/no: ')
        if confirmance == 'yes':
            with open(db_file, 'wb') as f:
                pickle.dump(vr, f, pickle.HIGHEST_PROTOCOL)
                print('DATA has been recorded!')

    @staticmethod
    def load_from_db():
        with open(db_file, 'rb') as f:
            VR = pickle.load(f)
        return VR


# main function to work with
def main():
    VR = VerkhovnaRada()
    while True:
        if 'entered' in locals():
            message = input('\npress Enter to continue...')

        choice = input("""
        Введіть 1, щоб додати фракцію
        Введіть 2, щоб видалити фракцію
        Введіть 3, щоб очистити фракцію
        Введіть 4, щоб вивести фракції
        Введіть 5, щоб видалити фракцію з ВР
        Введіть 6, щоб додати депутата у фракцію
        Введіть 7, щоб видалити депутата із фракції
        Введіть 8, щоб вивести список хабарників у фракції
        Введіть 9, щоб вивести список  хабарників у раді
        Введіть 10, щоб вивести найбільшого хабарника у раді
        Введіть 11, щоб вивести найбільшого хабарника у фракції.
        Введіть 12, щоб перевірити чи є дупутат у фракції
        Введіть 13, щоб перевірити чи є депутат у раді
        Введіть 14, дати хабара депутату!
        Введіть 15, вивести всіх депутатів у ВР
        Введіть 16, записати у БД
        Введіть 17, зчитати з БД
        
        Введіть 0, щоб вийти із програми.
        : """)
        try:
            choice = int(choice)
        except ValueError:
            print('Enter a number from the list')
            continue

        entered = True
        #pdb.set_trace()

        if choice == 1:
            fr_name = input('Please enter a fraction name: ')
            VR.add_fraction(Fraction(fr_name))

        elif choice == 2:
            fr_name = input('Please enter a fraction name to be deleted: ')
            VR.remove_fraction(Fraction(fr_name))

        elif choice == 3:
            fr_name = input('Please enter fraction name to work with: ')
            Fraction(fr_name).clean_out_deputies()

        elif choice == 4:
            VR.print_all_fractions()

        elif choice == 5:
            fr_name = input('Please enter a fraction name to be deleted: ')
            VR.remove_fraction(Fraction(fr_name))

        elif choice == 6:
            fr_name = input('Please enter fraction name to work with: ')
            fr = Fraction(fr_name)
            fr.add_deputy()

            VR.add_fraction(fr)

        elif choice == 7:
            fr_name = input('Please enter fraction name to work with: ')
            fr = Fraction(fr_name)
            dp = fr.add_deputy()

            VR.remove_deputy_from_fraction(dp, fr)

        elif choice == 8:
            fr_name = input('Please enter fraction name to work with: ')
            fr = Fraction(fr_name)

            if fr in VR.fractions:
                for fraction in VR.fractions:
                    if fraction == fr:
                        fraction.find_all_bribe_takers()

        elif choice == 9:
            VR.print_all_bribe_takers()

        elif choice == 10:
            VR.higher_bribe_taker()

        elif choice == 11:
            fr_name = input('Please enter fraction name to work with: ')
            fr = Fraction(fr_name)

            if fr in VR.fractions:
                for fraction in VR.fractions:
                    if fraction == fr:
                        fraction.find_highest_bribe_taker()

        elif choice == 12:
            fr_name = input('Please enter fraction name to work with: ')
            fr = Fraction(fr_name)
            dp = Deputat.describe_deputy()
            if dp:
                fr.is_participant(dp, VR)

        elif choice == 13:
            dp = Deputat.describe_deputy()
            if dp:
                VR.is_present_in_vr(dp)

        elif choice == 14:
            dp = Deputat.describe_deputy()
            if dp:
                dp.give_tribute()
                VR.update_deputy(dp)

        elif choice == 15:
            VR.print_all_deputies()

        elif choice == 16:
            VerkhovnaRadaDataBase.save_to_db(VR)

        elif choice == 17:
            VR = VerkhovnaRadaDataBase.load_from_db()

        elif choice == 0:
            break


# interactive terminal
main()
