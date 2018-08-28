import csv
from pymodm.connection import connect
from mongomodels import Departament, Client, Application


connect('mongodb://192.168.99.100:27017/bank', alias='default')
deps = dict()
clients = dict()


def upload_from_csv_and_add_to_bd():

    with open('department.csv', 'r') as c_file:
        reader = csv.reader(c_file)
        for n, row in enumerate(reader):
            if n == 0:
                pass
            else:
                departament = Departament(city=row[1], count_of_workers=row[2])
                deps[row[0]] = departament

    with open('client.csv', 'r') as x_file:
        reader = csv.reader(x_file)
        for n, row in enumerate(reader):
            if n == 0:
                pass
            else:
                client = Client(first_name=row[1], last_name=row[2], education=row[3],
                                passport=row[4], city=row[5], age=row[6])
                deps[row[7]].clients.append(client)
                clients[row[0]] = client

    with open('application.csv', 'r') as a_file:
        reader = csv.reader(a_file)
        for n, row in enumerate(reader):
            if n == 0:
                pass
            else:
                application = Application(sum=row[1], credit_state=row[2], currency=row[3])
                clients[row[4]].applications.append(application)

    for v in deps.values():
        v.save()


def custom_queries():
    departments = Departament.objects.all()
    for dep in departments:
        for client in dep.clients:
            print(client)
    print('1\n')


if __name__ == '__main__':
    upload_from_csv_and_add_to_bd()
    custom_queries()
    # import ipdb;ipdb.set_trace()
    # pass