import car

"""
Here I'm using these functions to show the inheritance, overwrite, and extra class uses
in order to not make a single class go on for....well, ever lol.
"""
my_tesla = car.ElectricCar('tesla', 'model s', 2019)
my_new_car = car.Car('toyota', 'prius', '2012')
my_used_car = car.Car('chevy', 's10', '1985')
print(my_new_car.get_discriptive_name())
my_new_car.fill_gas_tank()
print(my_tesla.get_discriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()  # Here we added 'battery' as part of the call
my_tesla.battery.get_range()  # Here I'm using the 'battery' again after adding a new function to the class

print("\n")
"""Verifying that the battery upgrade worked as intended"""
my_tesla.battery.describe_battery()  # Here I print out the battery description
print("Let's check about an upgrade")
my_tesla.battery.upgrade_battery()  # Run the upgrade module
my_tesla.battery.describe_battery()  # Print again to verify the upgrade module worked

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