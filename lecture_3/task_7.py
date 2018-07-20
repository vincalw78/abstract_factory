# -*- coding: utf-8 -*
# 7) Робота із info.csv файлом. У файлі вказано школи із Англії.
# 7.1) зчитати файл і помістити дані в певну структуру ( змінну)
# 7.2) (окрема ф-я) відфільтрувати дані де є вказано адресу сайту і зберегти в базі даних pickle
# 7.3) (окрема ф-я) відфільтрувати дані де директорами є Ms і Mrs. Потім зберегти у json файлі дані про
#    номер школи, місто, моб тел ( якщо є) , сайт ( якщо є), імя та прізвище директора.
# 7.4) Написати ф-ю яка рахує кількість відкритих шкіл після 2000 року. Надрукувати результат.
# 7.5) Відфільтрувати школи які вже є закритими, відповідно відкриті школи записати в файл оpened.csv
from datetime import datetime
import csv
import pickle
import json

eng_schools_csv = './files/info.csv'
pickle_emails = './files/pickle_emails.pickle'
json_headers = './files/school_headers.json'
opened_csv = './files/opened.csv'


# 7.1
def convert_to_obj(data):
    with open(eng_schools_csv, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            obj = {}
            for key in line:
                obj[key] = line[key]
            data.append(obj)
    return data


# 7.2
def filter_by_email(data):
    return [obj['SchoolWebsite'] for obj in data if obj['SchoolWebsite']]


def save_to_pickle(data):
    with open(pickle_emails, 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


# 7.3
def filter_by_sex(data):
    return [obj for obj in data if obj['HeadTitle (name)'] in ['Mrs', 'Ms']]


def save_to_json(data):
    keys = [
        'EstablishmentNumber', 'LA (name)', 'TelephoneNum', 'SchoolWebsite', 'HeadFirstName', 'HeadLastName'
    ]

    with open(json_headers, 'w') as f:
        json_obj = {}

        for index, obj in enumerate(data):
            filtered_data = {}

            for key in keys:
                filtered_data[key] = obj[key]

            json_obj[index] = filtered_data

        json.dump(json_obj, f, indent=4, sort_keys=True)


# 7.4
def print_new_schools(data):
    count = 0
    for obj in data:
        if obj['OpenDate']:
            if datetime.strptime(obj['OpenDate'], '%d-%m-%Y').year > datetime(2000, 1, 1).year:
                count += 1
    print('{} new schools have been opened since 2000'.format(count))


# 7.5 find closed schools, opened write into a csv file.
def filter_by_opened_and_write():
    with open(eng_schools_csv, 'r', encoding='utf-8') as f1, open(opened_csv, 'w', encoding='utf-8') as f2:
        csv_reader = csv.DictReader(f1)
        csv_writer = csv.DictWriter(f2, csv_reader.fieldnames)

        for line in csv_reader:
            if not line['CloseDate']:
                csv_writer.writerow(line)


if __name__ == '__main__':
    # returns list of objects.
    schools = []
    schools = convert_to_obj(schools)

    # filter by email and save to pickle db
    save_to_pickle(filter_by_email(schools))

    # filter by sex (Ms, Mrs) and convert to JSON
    save_to_json(filter_by_sex(schools))

    # find new schools opened after 2000, key: OpenDate, print count. example: 30-09-1980
    print_new_schools(schools)

    # write opened schools into opened.csv
    filter_by_opened_and_write()
