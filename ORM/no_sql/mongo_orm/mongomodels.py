from pymodm import MongoModel, EmbeddedMongoModel, fields


class Application(EmbeddedMongoModel):
    sum = fields.IntegerField()
    credit_state = fields.CharField()
    currency = fields.CharField()

    def __str__(self):
        return f'{self.sum}, {self.credit_state}, {self.currency}'


class Client(EmbeddedMongoModel):

    first_name = fields.CharField()
    last_name = fields.CharField()
    education = fields.CharField()
    passport = fields.CharField()
    city = fields.CharField()
    age = fields.CharField()
    applications = fields.EmbeddedDocumentListField(Application)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.education}, ' \
               f'{self.passport}, {self.city}, {self.age}'


class Departament(MongoModel):
    city = fields.CharField()
    count_of_workers = fields.IntegerField()
    clients = fields.EmbeddedDocumentListField(Client)

    def __str__(self):
        return f'{self.city}, {self.count_of_workers}'

