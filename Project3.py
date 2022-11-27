import pickle

#Menu Choice Variables
emp_search = 1
emp_add = 2
emp_change = 3
emp_del = 4
quit = 5

def main():

    #Empty Dictionary
    employees = {}

    #Variable for user choice
    choice = 0

    while choice != quit:
        # Get the user's menu choice.
        choice = get_menu_choice()

        # Process the choice.
        if choice == emp_search:
            search(employees)
        elif choice == emp_add:
            add(employees)
        elif choice == emp_change:
            change(employees)
        elif choice == emp_del:
            delete(employees)

    #Upon program exiting, try save dictionary to file, if can't, create file
    f = open("employeeData.dat", "wb")
    pickle.dump(employees, f)
    f.close()

# The get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    print()
    print('Employee Records')
    print('---------------------------')
    print('1. Look up a record')
    print('2. Add a record')
    print('3. Change a record')
    print('4. Delete a record')
    print('5. Quit')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < emp_search or choice > quit:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice

# The search function looks up a name in the
# employees dictionary.
def search(employees):
    # Get a name to look up.
    id = input('Enter employees ID: ')

    # Look it up in the dictionary.
    print(employees.get(id, 'Not found.'))

# The add function adds a new entry into the
# employees dictionary.
def add(employees):
    # Get a name and job description.
    id = input('Enter employee ID: ')
    emp_data = []
    emp_data.append(input('Enter name: '))
    emp_data.append(input('Enter department: '))
    emp_data.append(input('Enter job title: '))

    # If the name does not exist, add it.
    if id not in employees:
        employees[id] = emp_data
    else:
        #otherwise notify user it doesn't exist
        print('That entry already exists.')

# The change function changes an existing
# entry in the employees dictionary.
def change(employees):
    # Get an id to look up.
    id = input('Enter an ID: ')

    if id in employees:
        # Get new info
        id = input('Enter the new Employee ID: ')
        emp_data = []
        emp_data.append(input('Enter name: '))
        emp_data.append(input('Enter department: '))
        emp_data.append(input('Enter job title: '))

        # Update the entry.
        employees[id] = emp_data
    else:
        print('That name is not found.')

# The delete function deletes an entry from the
# employees dictionary.
def delete(employees):
    # Get an ID to look up.
    id = input('Enter an ID: ')

    # If the ID is found, delete the entry.
    if id in employees:
        del employees[id]
    else:
        print('That name is not found.')


main()
