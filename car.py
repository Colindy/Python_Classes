class Car:
    """A simple representation of a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to descrive a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_discriptive_name(self):
        """Return a formatted discriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the odometer reading"""
        print(f"This car's odometer reading is {self.odometer}.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the value in mileage
        Also, make sure the mileage can't be rolled back
        """
        if mileage >= self.odometer:
           self.odometer = mileage
        else:
            print("You can't roll back the odometer!!")
    def increment_odometer(self, miles):
        """Adds the given amount to the odometer"""
        self.odometer += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Then initialize attributes of the child class
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery"""
        print(f"This car has a {self.battery_size}-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
my_new_car = Car('toyota', 'prius', '2012')
my_used_car = Car('chevy', 's10', '1985')
print(my_new_car.get_discriptive_name())
print(my_tesla.get_discriptive_name())
my_tesla.describe_battery()
print("\n")
#my_new_car.odometer = 23  # Here we edit the odometer reading directly by assigning it a new value
my_new_car.update_odometer(35)   # Here we use the module inside the Class to update the mileage
my_new_car.read_odometer()
print("\n")
"""Here we're going to check the 'rollback' check in update_odometer"""
print(my_used_car.get_discriptive_name())
my_used_car.update_odometer(285_835)
my_used_car.read_odometer()
print("\n")
my_used_car.increment_odometer(500) # Here we increment the odometer
my_used_car.read_odometer()
print("\n")
my_used_car.update_odometer(2_500) # Here we test the rollback check
my_used_car.read_odometer()
print("\n")