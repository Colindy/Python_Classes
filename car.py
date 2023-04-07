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

    def upgrade_battery(self):
        """Look and see if the battery can be upgraded"""
        if self.battery_size < 100:
            self.battery_size = 100
        else:
            print("This battery does not need upgraded.")

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
