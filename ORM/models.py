from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class Departament(Base):
    __tablename__ = 'departament'

    id = Column(Integer, primary_key=True)
    city = Column(String)
    count_of_workers = Column(Integer)

    def __str__(self):
        return f'{self.id}, {self.city}, {self.count_of_workers}'


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    education = Column(String)
    passport = Column(String)
    city = Column(String)
    age = Column(String)
    departament_id = Column(Integer, ForeignKey('departament.id'))
    departament = relationship('Departament', backref=backref('clients', order_by=id))

    def __str__(self):
        return f'{self.id}, {self.first_name}, {self.last_name}, {self.education}, ' \
               f'{self.passport}, {self.city}, {self.age}, {self.departament_id}, ' \
               f'{self.departament}'


class Application(Base):
    __tablename__ = 'application'

    id = Column(Integer, primary_key=True)
    sum = Column(Integer)
    credit_state = Column(String)
    currency = Column(String)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship('Client', backref=backref('applications', order_by=id))
    
    def __str__(self):
        return f'{self.id}, {self.sum}, {self.credit_state}, {self.currency}, {self.client_id},' \
               f'{self.client}'
