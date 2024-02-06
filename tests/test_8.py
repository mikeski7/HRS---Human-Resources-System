import csv
import os.path
import sys

# paths to local files
path_table = './table.csv'
path_emp_data = './emp_data.csv'

employees_load = []
row_to_del = []
duplicates = []

# Check if the file with employees' data has been created
if not os.path.isfile(path_emp_data):
    print('No data to be deleted. Please add at least one employee to the database to proceed with the operation.')
# If so, proceed with the delete proccess
else:
    with open('emp_data.csv', 'r') as infile:
        reader = csv.reader(infile)
        while True:
            print('Please type the following data:')
            first = input('First: ').strip().capitalize()
            last = input('Last: ').strip().capitalize()
            counter = 0
            for row in reader:
                employees_load.append(row)
                if row[0] == first and row[1] == last:
                    # Appends the number of the row in the oryginal file to the list
                    row_to_del.append(reader.line_num)
                    # Appends the duplicated data to the list
                    duplicates.append(row)
                    # Counter counts how many duplicates there are
                    counter += 1
            if counter == 0:
                ans = input('No employee matches your search. Do you want to try again (Y/N)?').capitalize()
                if ans == 'Y' or ans == 'YES':
                    pass
                else:
                    sys.exit('No employee has been deleted.')
            else:
                break

    with open('emp_data.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        if counter == 1:
            for i in range(len(employees_load)):
                row = employees_load[i]
                if i+1 != row_to_del[0]:
                    writer.writerow(row)
        else:
            for i in range(len(duplicates)):
                print(i+1, ' - ', duplicates[i])
            number = int(input('Which employee of the displayed above you want to delete? Please type the appropriate number: '))
            for i in range(len(employees_load)):
                row = employees_load[i]
                if i+1 != row_to_del[number-1]:
                    writer.writerow(row)