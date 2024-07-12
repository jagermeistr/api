class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, registration_number, make, model, num_seats):
        super().__init__(registration_number, make, model)
        self.num_seats = num_seats

class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        for vehicle in self.vehicles:
            print(f"Registration Number: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}")

    def search_vehicle(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                print(f"Registration Number: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}")
                return
        print("Vehicle not found")

fleet = Fleet()
fleet.add_vehicle(Car("KBX 166A", "Toyota", "Proobox", 5))
fleet.add_vehicle(Truck("KDA 456A", "Isuzzu", "FRR",5000))
fleet.add_vehicle(Motorcycle("KMDA 456A", "Boxer", "150 UG",150))
fleet.display_vehicles()
fleet.search_vehicle("KMDA 456A") 
print()
fleet.search_vehicle("KMDB 456A") 
print()

