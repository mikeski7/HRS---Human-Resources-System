import csv
from tabulate import tabulate
import os.path


employees = []

# Asks for employee data and appends the data to a listas a dictionary, in case of end of data typing, breaks out of nested loop.
while True:
    first = input('First: ')
    last = input('Last: ')
    employees.append({'First': first, 'Last': last})
    while True:
        action = input('Do you want to add another employee? (Y/N) ')
        if action == 'Y':
            break
        elif action == 'N':
            break
        else:
            pass
    if action == 'N':
        break

# Appends the data to an external .csv file
with open('emp_data.csv', 'a') as f:
    writer = csv.writer(f)
    for employee in employees:
        w = [employee['First'], employee['Last']]
        writer.writerow(w)