import csv
import os.path

# paths to local files
path_table = './table.csv'
path_emp_data = './emp_dats.csv'

employees_load = []
row_to_del = []
duplicates = []

# Check if the file with employees' data has been created
if not os.path.isfile(path_emp_data):
    print('No data to be deleted. Please add at least one employee to the database to proceed with the operation.')
# If so, proceed with the delete proccess
else:
    with open('emp_dats.csv', 'r+') as infile:
        reader = csv.reader(infile)
        for row in reader:
            print(reader.line_num)
            '''if row[0] == first and row[1] == last:
                # Appends the number of the row in the oryginal file to the list
                row_to_del.append(reader.line_num)
                # Appends the duplicated data to the list
                duplicates.append(row)
                # Counter counts how many dyplicates there are
                counter += 1
        if counter == 0:
            print('No employee matches your search. Please try again.')
        elif counter == 1:
            print(row_to_del[0])
            for row in reader:
                print(reader.line_num)
                if reader.line_num == row_to_del[0]:

                    pass
                else:
                    writer.writerow(row)'''
        '''else:
            address = input('More than one employee has been found. Please specify the address: ').strip().capitalize()
            print(duplicates)
            for row in duplicates:
                if row[2] == address:
                    reader.pop(row_to_del[row.line_num])

        for row in reader:
            print(row)'''