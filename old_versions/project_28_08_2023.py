'''programme name: HRS - Human Resources System'''

import csv
from tabulate import tabulate
import os.path
import inspect

# paths to local files
path_table = './table.csv'
path_emp_data = './emp_data.csv'

'''# Create a class
class Employee:
    def __init__(self, first, last, address, telephone, grade, salary):
        self.first = first
        self.last = last
        self.address = address
        self.telephone = telephone
        self.grade = grade
        self.salary = salary'''

def main():

    # Displays options function
    options()

    # Get the operation number
    choice = int(input('Please choose the option: '))

    if choice == 1:
        add_employee()
    elif choice == 2:
        delete_employee()
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

    '''try:
        with open('emp_data.csv', 'r') as f:
            reader = csv.reader(f)
            lines = int(len(list(reader)))
    except FileNotFoundError:
        lines = 0

    num_of_arg = len(inspect.getfullargspec(__init__).args)

    print(num_od_arg)'''

    '''for i in range(num_of_arg):
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
                sys.exit('')'''

    # Creates an empty list as a global variable
    global employees
    employees = []

    # Asks for employee data and appends the data to a list, in case of end of data typing breaks out of nested loop
    while True:
        first = input('First: ')
        last = input('Last: ')
        nationality = input('Nationality: ')
        address = input('Address: ')
        city = input('City: ')
        number = input('Tel. number: ')
        employee = {
            'First': first,
            'Last': last,
            'Nationality': nationality,
            'Address': address,
            'City': city,
            'Number': number
        }

        # Capitalizes all the data except tel. number
        for key in employee:
            if key == 'Number':
                continue
            else:
                employee[key] = employee[key].strip().capitalize()

        employees.append(employee)
        while True:
            action = input('Do you want to add another employee? (Y/N) ')
            if action == 'Y' or action == 'y':
                break
            elif action == 'N' or action == 'n':
                break
            else:
                pass
        if action == 'N':
            break

    # Appends the data to an external .csv file
    with open('emp_data.csv', 'a') as f:
        writer = csv.writer(f)
        for employee in employees:
            w = [employee['First'], employee['Last'], employee['Nationality'], employee['Address'], employee['City'], employee['Number']]
            writer.writerow(w)

def delete_employee():

    employees_load = []

    # Check if the file with employees' data has been created
    if not os.path.isfile(path_emp_data):
        print('No data to be deleted. Please add at least one employee to the database to proceed with the operation.')
    # If so, proceed with the delete proccess
    else:
        with open('emp_data.csv', 'r') as infill:
            reader = csv.reader(infile)
            first = input('First: ').strip().capitalize()
            last = input('Last: ').strip().capitalize()
            for row in reader:
                if row[0] == first and row[1] == last:
                    print('Dupa')

        '''writer = csv.writer(output)
        for row in csv.reader(input):
            w = [employee['First'], employee['Last'], employee['Nationality'], employee['Address'], employee['City'], employee['Number']]
            writer.writerow(w)

    import csv
input = open('first.csv', 'rb')
output = open('first_edit.csv', 'wb')
writer = csv.writer(output)
for row in csv.reader(input):
    if row[2]!=0:
        writer.writerow(row)
input.close()
output.close()

    first = input('Please enter employee first name: ').strip().capitalize()
    last = input('Please enter employee last name: ').strip().capitalize()'''

if __name__ == '__main__':
    main()