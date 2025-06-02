from datetime import datetime

employees_filepath = "./employees.txt"
current_month = datetime.now().month
birthdays = {}

def find_birthdays_this_month(filepath):
    try:
        with open(filepath, 'r') as employees:
            for employee in employees:

                # We are assuming the lines are in the format <FirstName> <LastName>, mm/dd/YYYY
                name, dob = employee.split(", ", 1)
                birthday = datetime.strptime(dob.strip(), "%d/%m/%Y")

                if birthday.month == current_month:
                    day = dob.split("/")[0]
                    birthdays[name] = day

    except FileNotFoundError:
        print("Error: File not found!")

    return birthdays

if find_birthdays_this_month(employees_filepath):
    print("We would like to wish the following employees a happy birthday this month!")
    for key in birthdays:
        print(f"{key}, who is celebrating on {current_month}/{birthdays[key]}")
else:
    print("There are no employees with birthdays this month.")