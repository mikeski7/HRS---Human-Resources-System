import csv
employees = []

# Do-While loop has been created out of While loop and if statement. Creates a dictionary and if so, appends employees to employees list.
while True:
    first = input('First: ')
    last = input('Last: ')
    number = input('Tel. number: ')
    employee = {
        'First': first,
        'Last': last,
        'Number': number
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

'''for key in employee:
        if key == 'Number':
            print(employee[key])
            continue
        else:
            employee[key] = employee[key].strip().upper()
            print(employee[key])

    employees.append(employee)
    while True:
        action = input('Do you want to add another employee? (Y/N) ').upper()
        if action == 'Y' :
            break
        elif action == 'N':
            break
        else:
            pass
    if action == 'N':
        break'''