'''programme name: HRS - Human Resources System'''

import csv
from tabulate import tabulate
import os.path
import inspect

# paths to local files
path_table = './table.csv'
path_emp_data = './emp_data.csv'


def main():

    # Displays options function
    options()

    # Get the operation number
    choice = int(input('Please choose the option: '))

    if choice == 1:
        add_employee()
    elif choice == 2:
        delete_employee()
    elif choice == 3:
        search_employee()
    elif choice == 4:
        change_employee()
    elif choice == 5:
        display_employee()
    else:
        print('Coś poszło nie tak!')

def options():
    # Creates title for the menu and a new table.
    headers = [['   Human   Resources   System  ']]
    table = []

    # Creates a list of lists. Single nested list comprises of one row from table.csv
    try:
        with open('table.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
    except FileNotFoundError:
        print('Incorrect name. Please check the file named table.csv')
        exit()

    # Prints teh tables in the required format.
    print((tabulate(headers, tablefmt="grid")))
    print((tabulate(table, tablefmt="grid")))

def add_employee():

    employees = []

    # Do-While loop has been created out of While loop and if statement. Creates a dictionary and if so, appends employees to employees list.
    while True:
        first = input('First: ').strip()
        last = input('Last: ').strip()
        address = input('Address: ').strip()
        city = input('City: ').strip()
        number = input('Tel. number: ').strip()
        grade = input('Grade: ').strip()
        position = input('Position: ').strip()
        unit = input('Unit: ').strip()
        employee = {
            'First': first,
            'Last': last,
            'Address':  address,
            'City': city,
            'Number': number,
            'Grade': grade,
            'Position': position,
            'Unit': unit
        }
        employees.append(employee)
        action = input('Do you want to add another employee? (Y/N) ').upper()
        if action == 'Y' :
            pass
        elif action == 'N':
            break

    # Appends the data to an external .csv file
    with open('emp_data.csv', 'a') as f:
        writer = csv.writer(f)
        for employee in employees:
            line = [employee['First'], employee['Last'], employee['Number']]
            writer.writerow(line)

def delete_employee():

    employees_load = []

    # Check if the file with employees' data has been created
    if not os.path.isfile(path_emp_data):
        print('No data to be deleted. Please add at least one employee to the database to proceed with the operation.')
    # If so, proceed with the delete proccess
    else:
        with open('emp_data.csv', 'r') as infile:
            reader = csv.reader(infile)
            print('Please type the following data:')
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