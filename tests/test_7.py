import csv
import os.path

try:
    with open('emp_dats.csv', 'a') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
except FileNotFoundError:
    print('finito')

    first = input('First: ')
    last = input('Last: ')
    number = input('Tel. number: ')
    employee = {
        'First': first,
        'Last': last,
        'Number': number
    }