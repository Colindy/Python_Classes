from user import *
from admin import *


user1 = User("Eric", "Bradshaw", "58648", "AzzKicking")
user2 = User("Steve", "Austin", "316", "Rattlesnake")
user3 = User("Stacy", "Keibler", "69696", "PinUp")
user4 = User("Jeff", "Hardy", "489456", "High Flying Cool Brother")
user5 = Admin("Ahska", "Unknown", "56813", "Boss")

"""
Now let's do some stuff with our users
First user here
"""

user1.full_name()
user1.dept()
user1.greet()
print(user1.login_attempts) # Print attempts here to verify the count
user1.increment_login_attempts(1)
print(user1.login_attempts) # Print them here to verify the counter of 1
user1.reset_login_attempts()
print(user1.login_attempts) # Print here again to verify that reset worked

"""Second user"""
print("\n")
user2.full_name()
user2.greet()

"""Third user"""
print("\n")
user3.full_name()
user3.who()
user3.greet()

"""Fourth user"""
print("\n")
user4.full_name()
user4.who()
user4.dept()
user4.greet()

"""Admin user"""
print("\n")
user5.full_name()
user5.privileges.show_privileges()
