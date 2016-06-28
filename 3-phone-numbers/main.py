import csv
import sys
from person import Person


def open_csv(file_name):
    with open(file_name) as f:
        data = []
        for i in f:
            i.rstrip("\n").split(",")
            data.append(i)
    return data


def get_csv_file_name(argv_list):
    try:
        return argv_list[1]
    except:
        pass

def format_output(person):
    if person != None:
        return "This number belongs to: {0}".format(person.get_name())
    else:
        return "No match found."



def get_person_by_phone_number(person_list, user_input_phone_number):
    for i in person_list:
        if i.is_phone_number_matching(user_input_phone_number):
            return i
        else:
            pass


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
