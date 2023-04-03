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

    def fill_gas_tank(self):
        """
        Gives an amount of gas to add to the car
        Also gives us a handy way to show parent class method overwrite
        """
        print("We need to fill the gas tank!!")

class Battery:
    """A simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=75):
        """Initialize the battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Then initialize attributes of the child class
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """We don't need gas for the electric car"""
        print("We don't need no stinkin gas!!  It's electric!")



"""
Here I'm using these functions to show the inheritance, overwrite, and extra class uses
in order to not make a single class go on for....well, ever lol.
"""
my_tesla = ElectricCar('tesla', 'model s', 2019)
my_new_car = Car('toyota', 'prius', '2012')
my_used_car = Car('chevy', 's10', '1985')
print(my_new_car.get_discriptive_name())
my_new_car.fill_gas_tank()
print(my_tesla.get_discriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()  # Here we added 'battery' as part of the call
my_tesla.battery.get_range()  # Here I'm using the 'battery' again after adding a new function to the class

print("\n")
#my_new_car.odometer = 23  # Here we edit the odometer reading directly by assigning it a new value (commented out after edits)
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