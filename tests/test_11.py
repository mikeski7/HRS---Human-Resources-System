import csv
import os.path
import sys

# paths to local files
path_table = './table.csv'
path_emp_data = './emp_data.csv'

employees_load = []
emp_to_disp = []
duplicates = []

# Check if 'emp_data' file has been created
if not os.path.isfile(path_emp_data):
    print('No data to be displayed. Please add at least one employee to the database to proceed with the operation.')
# If so, proceed with the display
else:
    with open('emp_data.csv', 'r') as infile:
        reader = csv.reader(infile)
        while True:
            print('Please type the following data:')
            first = input('first name: ').strip().capitalize()
            last = input('last name: ').strip().capitalize()
            counter = 0
            for row in reader:
                if row[0] == first and row[1] == last:
                    # Appends the employees data to the list
                    duplicates.append(row)
                    # Counter counts how many employees there are
                    counter += 1
            if counter == 0:
                ans = input('No employee matches your search. Do you want to try again (Y/N)? ').capitalize()
                if ans == 'Y' or ans == 'YES':
                    pass
                else:
                    sys.exit('No employee has been found.')
            elif counter == 1:
                print('1 employee has been found:\n', duplicates[0], sep='')
                break
            else:
                print(f'{counter} employees have been found:')
                for i in range(len(duplicates)):
                    print(f'{i+1} - {duplicates[i]}')
                break