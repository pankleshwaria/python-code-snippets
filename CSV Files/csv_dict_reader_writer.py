import csv

with open('employee_info.csv', mode='r') as csv_file:
    fieldnames = ['first-name', 'last-name', 'email']
    csv_reader = csv.DictReader(csv_file, fieldnames=fieldnames)

    # next to avoid field header
    next(csv_reader)

    for row in csv_reader:
        print(row['email'])

# Copying csv file
print('Copying csv file...')
with open('employee_info.csv', mode='r', encoding='utf-8') as csv_file:
    with open('employee_info_copy.csv', mode='w', encoding='utf-8') as new_file:
        fieldnames = ['first-name', 'last-name', 'email']
        csv_reader = csv.DictReader(csv_file, fieldnames=fieldnames)

        csv_writter = csv.DictWriter(new_file, fieldnames=fieldnames)
        csv_writter.writeheader()

        # next to avoid field header
        next(csv_reader)

        for row in csv_reader:
            print(f'Copying data for {row["first-name"]} {row["last-name"]}')
            csv_writter.writerow(row)
