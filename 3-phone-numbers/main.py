import csv
import sys
from person import Person
import csv


def open_csv(file_name):
    with open(file_name) as f:
        data = list(csv.reader(f))
        data = [Person(i[0], i[1]) for i in data]
    print(data[1]._phone_number)
    return data


def get_csv_file_name(argv_list):
    try:
        return argv_list[1]
    except:
        pass


def format_output(person):
    if person is None:
        return "No match found."
    elif type(person) == Person:
        return "This number belongs to: {0}".format(person.get_name())
    else:
        return "This number may belong to: {0}".format(", ".join([i.get_name() for i in person]))


def get_person_by_phone_number(person_list, user_input_phone_number):
    matching = [i for i in person_list if i.is_phone_number_matching(user_input_phone_number)]
    if len(matching) == 1:
        return matching[0]
    elif len(matching) > 1:
        return matching

def main():
    file_name = get_csv_file_name(sys.argv)
    if file_name is None:
        print('No database file was given.')
        sys.exit(0)

    person_list = open_csv(file_name)
    user_input_phone_number = input('Please enter the phone number: ')
    match_person = get_person_by_phone_number(person_list, user_input_phone_number)

    print(format_output(match_person))

if __name__ == '__main__':
    main()
