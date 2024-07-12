
patients = []

def add_patient(name, age, illness):
    patient = {"name": name, "age": age, "illness": illness}
    patients.append(patient)

def display_patients():
    for patient in patients:
        print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")

def search_patient(name):
    for patient in patients:
        if patient["name"] == name:
            print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
            return
    print("Patient not found")

def remove_patient(name):
    global patients
    patients = [patient for patient in patients if patient["name"] != name]

while True:
    print("1. Add patient")
    print("2. Display patients")
    print("3. Search patient")
    print("4. Remove patient")
    print("5. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Enter patient name: ")
        age =int(input("Enter patient age: ").strip())
        illness = input("Enter patient illness: ")
        add_patient(name, age, illness)
    elif choice == "2":
        display_patients()
    elif choice == "3":
        name = input("Enter patient name to search: ")
        search_patient(name)
    elif choice == "4":
        name = input("Enter patient name to remove: ")
        remove_patient(name)
    elif choice == "5":
        break
    else:
        print("Invalid option. Please Try again")
