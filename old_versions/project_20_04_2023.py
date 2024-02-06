'''programme name: HRS - Human Resources System'''

import csv
from tabulate import tabulate
import os.path
import inspect

def main():

    class Employee:
        def __init__(self, first, last, address, telephone, grade, salary):
            self.first = first
            self.last = last
            self.address = address
            self.telephone = telephone
            self.grade = grade
            self.salary = salary

    options()

    choice = int(input('Please choose the option: '))

    fname = 'Michal'
    lname = 'Kowalski'

    if choice == 1:
        add_employee()
    else:
        print('Coś poszło nie tak!')

def options():
    headers = [['   Human   Resources   System  ']]
    table = []

    try:
        with open('table.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
    except FileNotFoundError:
        print('Incorrect name. Please check the file named table.csv')
        exit()


    print((tabulate(headers, tablefmt="grid")))
    print((tabulate(table, tablefmt="grid")))

def add_employee():

    try:
        with open('emp_data.csv', 'r') as f:
            reader = csv.reader(f)
            lines = int(len(list(reader)))
    except FileNotFoundError:
        lines = 0

    num_of_arg = len(inspect.getfullargspec(__init__).args)

    for i in range(num_of_arg):
        emp_1.inspect.getfullargspec(__init__)[i] = input(inspect.getfullargspec(__init__)[i] + ': ')

    emp_blueprint = 'emp_' + str(lines + 1)
    emp_blueprint = Employee()
    emp_blueprint.first = input('first name: ')
    emp_blueprint.last = input('last name: ')
    emp_blueprint.address = input('address: ')
    emp_blueprint.telephone = input('telephone: ')
    emp_blueprint.grade = input('grade: ')
    emp_blueprint.salary = input('salary: ')

    fname = 'Michal'
    lname = 'Kowalski'
    employee_data = []
    path = './emp_data.csv'
    if os.path.isfile(path):
        operation = 'a'
    else:
        operation = 'w'
    with open('emp_data.csv', operation) as f:
        try:
            writer = csv.writer(f)
            writer.writerow([fname])
        except FileNotFoundError:
                sys.exit('')


if __name__ == '__main__':
    main()