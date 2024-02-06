'''programme name: HRS - Human Resources System'''

from cs50 import SQL
import csv
import sys

# paths to local files
path_table = './table.csv'
path_emp_data = './emp_data.csv'

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")

def main():

    # Displays options function
    options()

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
    print(headers[0][0])
    for list in table:
        print(list[0],' -',list[1], sep='')

    # Get the operation number
    choice = int(input('Please choose the option below: '))

    if choice == 1:
        add_employee()
    elif choice == 2:
        delete_employee()
    elif choice == 3:
        search_employee()
    elif choice == 4:
        change_employee()
    elif choice == 5:
        quit()
    else:
        print('Please type the appropriate number 1-5')

def add_employee():

    # Get data from user
    while True:
        first = input('First: ').strip().capitalize()
        last = input('Last: ').strip().capitalize()
        address = input('Address: ').strip().capitalize()
        city = input('City: ').strip().capitalize()
        tel_num = input('Tel. number: ').strip()
        grade = input('Grade: ').strip()
        position = input('Position: ').strip()
        unit = input('Unit: ').strip()
        db.execute("INSERT INTO employees (first, last, address, city, tel_num, grade, position, unit) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   first, last, address, city, tel_num, grade, position, unit)
        print('Employee has been sucessfully added.')
        action = input('Do you want to add another employee? (Y/N) ').upper()
        if action == 'Y' or action == 'YES':
            pass
        elif action == 'N':
            options()

def delete_employee():

    employees_load = db.execute("SELECT * FROM employees")
    counter = 0

    # Check if the file with employees' data has been created
    if len(employees_load) < 1:
        print('No data to be deleted. Please add at least one employee to the database to proceed with the operation.')
    # If so, proceed with the delete proccess
    else:
        while True:
            print('Please type the following data:')
            first = input('first name: ').strip().capitalize()
            last = input('last name: ').strip().capitalize()
            position = input('position: ').strip()
            counter = 0
            for row in employees_load:
                if row['first'] == first and row['last'] == last and row['position'] == position:
                    # Counter counts how many duplicates there are
                    counter += 1
            if counter == 0:
                # No employee has been found
                ans = input('No employee matches your search. Do you want to try again (Y/N)?').capitalize()
                if ans == 'Y' or ans == 'YES':
                    pass
                else:
                    sys.exit('No employee has been deleted.')
            elif counter == 1:
                # Remove employee
                db.execute("DELETE FROM employees WHERE first = ? AND last = ? AND position = ?", first, last, position)
                print('Employee has been sucessfully deleted.')
                return options()
            else:
                # Exit with a message
                sys.exit('Too many employees with the same position, first and last name have been added. Error!')


def search_employee():

    employees_load = db.execute("SELECT * FROM employees")

    # Check if 'emp_data' file has been created
    if len(employees_load) < 1:
        print('No data to be changed. Please add at least one employee to the database to proceed with the operation.')
    # If so, proceed with the display
    else:
        while True:
            print('Please type the following data:')
            first = input('first name: ').strip().capitalize()
            last = input('last name: ').strip().capitalize()
            position = input('position: ').strip()
            employee = db.execute("SELECT * FROM employees where first = ? AND last = ? AND position = ?", first, last, position)
            counter = 0
            for row in employees_load:
                if row['first'] == first and row['last'] == last and row['position'] == position:
                    counter += 1
            if counter == 0:
                # No employee has been found
                ans = input('No employee matches your search. Do you want to try again (Y/N)? ').capitalize()
                if ans == 'Y' or ans == 'YES':
                    pass
                else:
                    sys.exit('No employee has been found.')
            elif counter == 1:
                # Display employee
                print('1 employee has been found:\n')
                for key, value in employee[0].items():
                    if key == 'id':
                        pass
                    else:
                        print(key,': ', value, sep='')
                return options()
            # Exit with a message
            else:
                sys.exit('Too many employees with the same position, first and last name have been added. Error!')

def change_employee():
    employees_load = db.execute("SELECT * FROM employees")
    counter = 0

    # Check if the file with employees' data has been created
    if len(employees_load) < 1:
        print("No employee's data to be changed. Please add at least one employee to the database to proceed with the operation.")
    # If so, proceed with the delete proccess
    else:
        while True:
            print('Please type the following data:')
            first = input('first name: ').strip().capitalize()
            last = input('last name: ').strip().capitalize()
            position = input('position: ').strip()
            employee = db.execute("SELECT * FROM employees where first = ? AND last = ? AND position = ?", first, last, position)
            # Check how many employees there are
            for row in employees_load:
                if row['first'] == first and row['last'] == last and row['position'] == position:
                    counter += 1
            # If there's no match
            if counter == 0:
                ans = input('No employee matches your search. Do you want to try again (Y/N)? ').capitalize()
                if ans == 'Y' or ans == 'YES':
                    pass
                else:
                    sys.exit('No employee has been found.')
            # If there's one match
            elif counter == 1:
                print('1 employee has been found:\n')
                for key, value in employee[0].items():
                    if key == 'id':
                        pass
                    else:
                        print(key,': ', value, sep='')
                data = input('What data would you like to change? (Select one: first, last, address, city, tel_num, grade, position, unit) ')
                value = input('To what value?: ')
                db.execute("UPDATE employees SET " + data + " = ? WHERE first = ? AND last = ? AND position = ?", value, first, last, position)
                print(f"{first} {last}'s {data} has been sucessfully changed to {value}.")
                ans = input('Do you want to change more data? (Y/N)? ')
                if ans == 'Y' or ans == 'YES':
                    pass
                else:
                    break
            # Exit with a message
            else:
                sys.exit('Too many employees with the same position, first and last name have been added. Error!')

def quit():
    return

def shout(first='name', last='surname', position='position'):
    return f"{first} {last} the {position}"

def payrise(first='name', last='surname', new_sal='x'):
    return f"{first} {last} salary has been increased to {new_sal}"

def telephone(first='name', last='surname', tel_num='nobody knows what'):
    return f"{first} {last} phone number has changed to {tel_num}"

if __name__ == '__main__':
    main()