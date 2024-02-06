import csv

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_attributes(self):
        self.name = input('Name: ')
        self.age = input('Name: ')

# Creates an empty list as a global variable
global list
list = []

# Asks for employee data and appends the data to a list, in case of end of data typing breaks out of nested loop
while True:
    employee = Employee()
    employee.get_attributes()
    list.append([employee.name,' ' + employee.age])
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
    for i in range(len(list)):
        writer.writerow(list[i])