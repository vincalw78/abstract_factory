import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Departament, Client, Application, Base

engine = create_engine('sqlite:///bank.db')

Session = sessionmaker(bind=engine)
session = Session()


def create_all_tables():
    Base.metadata.create_all(engine)


def upload_from_csv_and_add_to_bd():

    with open('department.csv', 'r') as c_file:
        reader = csv.reader(c_file)
        for n, row in enumerate(reader):
            if n == 0:
                pass
            else:
                departament = Departament(city=row[1], count_of_workers=row[2])
                session.add(departament)

    with open('client.csv', 'r') as x_file:
        reader = csv.reader(x_file)
        for n, row in enumerate(reader):
            if n == 0:
                pass
            else:
                client = Client(first_name=row[1], last_name=row[2], education=row[3],
                                passport=row[4], city=row[5], age=row[6], departament_id=row[7])
                session.add(client)

    with open('application.csv', 'r') as a_file:
        reader = csv.reader(a_file)
        for n, row in enumerate(reader):
            if n == 0:
                pass
            else:
                application = Application(sum=row[1], credit_state=row[2], currency=row[3],
                                          client_id=row[4])
                session.add(application)
    session.commit()


def custom_queries():
    res = session.query(Application).order_by(Application.id.desc())[-5:]
    for client in res:
        print(client)


if __name__ == '__main__':
    create_all_tables()
    upload_from_csv_and_add_to_bd()
    custom_queries()
    # import ipdb;ipdb.set_trace()
    # pass