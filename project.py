import os
import time

class Business:
    def __init__(self, name):
        self.business_name = name

class Worker(Business):
    def __init__(self):
        super().__init__('')
        self.worker_name = ''
        self.worker_id = 0
        self.worker_department = ''
        self.worker_position = ''
        self.worker_wage = 0
        self.worker_data = {}

    def add_worker(self, name, business_name, id_number, department, position, hours):
        if name.isdigit():
            print("Validation Error: Worker's name can't be a number.")
            return
        if not name.isalpha():
            print("Validation Error: Worker's name must contain only letters.")
            return

        if not business_name.isalpha():
            print("Validation Error: Business name must contain only letters.")
            return
        if not department.isalpha():
            print("Validation Error: Department must contain only letters.")
            return
        if not position.isalpha():
            print("Validation Error: Position must contain only letters.")
            return

        if not isinstance(id_number, int):
            print("Validation Error: ID number must be an integer.")
            return
        if not isinstance(hours, int):
            print("Validation Error: Working hours must be an integer.")
            return

        self.worker_name = name
        self.business_name = business_name
        self.worker_id = id_number
        self.worker_department = department
        self.worker_position = position
        self.worker_hours = hours
        self.calculate_wage(hours)
        self.worker_data[self.worker_name] = [self.worker_id, self.business_name, self.worker_department, self.worker_position, self.worker_wage, self.worker_hours]

    def show_worker(self):
        if not self.worker_data:
            print("No worker data found.")
        else:
            print("\nWorker Details:")
            for name, data in self.worker_data.items():
                print("Worker's Name:", name)
                print("ID Number:", data[0])
                print("Business:", data[1])
                print("Department:", data[2])
                print("Position:", data[3])
                print("Wage:", data[4])
                print("Working Hours:", data[5])
                print()

    def search_worker(self, name):
        if name in self.worker_data:
            data = self.worker_data[name]
            print("Worker's ID Number:", data[0])
            print("Worker is associated with Business:", data[1])
            print("Worker's Department:", data[2])
            print("Worker's Position:", data[3])
            print("Worker's Monthly Wage: Rs", data[4])
            print("Worker's Monthly Working Hours:", data[5])
        else:
            print("Worker not found in records")

    def calculate_wage(self, hours):
        self.worker_wage = 10000 * hours

worker_object = Worker()

while True:
    print("\nOptions:")
    print("1. Add Worker")
    print("2. Search Worker")
    print("3. Display All Workers")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter Worker's Name: ")
        if name.isdigit():
            print("Worker's name can't be a number.")
            time.sleep(4)
            os.system('cls')
            continue

        business_name = input("Enter Business Name: ")
        if not business_name.isalpha():
            print("Business name must contain only letters.")
            time.sleep(4)
            os.system('cls')
            continue

        try:
            id_number = int(input("Enter ID Number: "))
        except ValueError:
            print("ID number must be an integer.")
            time.sleep(4)
            os.system('cls')
            continue

        department = input("Enter Department: ")
        if not department.isalpha():
            print("Department must contain only letters.")
            time.sleep(4)
            os.system('cls')
            continue

        position = input("Enter Position: ")
        if not position.isalpha():
            print("Position must contain only letters.")
            time.sleep(4)
            os.system('cls')
            continue

        try:
            hours = int(input("Enter Working Hours: "))
        except ValueError:
            print("Working hours must be an integer.")
            time.sleep(4)
            os.system('cls')
            continue

        worker_object.add_worker(name, business_name, id_number, department, position, hours)
        print("Worker added successfully!")
        time.sleep(4)
        os.system('cls')

    elif choice == '2':
        name = input("Enter Worker's Name: ")
        worker_object.search_worker(name)
        time.sleep(4)
        os.system('cls')

    elif choice == '3':
        worker_object.show_worker()
        time.sleep(4)
        os.system('cls')

    elif choice == '4':
        print("Exiting the program.")
        time.sleep(4)
        os.system('cls')
        break

    else:
        print("Invalid choice! Please select a valid option.")
        time.sleep(4)
        os.system('cls')
