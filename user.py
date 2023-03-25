class User:
    """A class to define a 'user'"""
    def __init__(self, fname, lname, id, department):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.department = department
        self.login_attempts = 0

    def full_name(self):
        print(f"User's full name is {self.fname} {self.lname}.\n")

    def who(self):
        print(f"{self.fname}'s ID number is {self.id}.\n")

    def dept(self):
        print(f"{self.fname} works in the {self.department} department.\n")

    def greet(self):
        print(f"Welcome {self.fname} {self.lname}!  Good to see you!\n")
        
    def increment_login_attempts(self, total_attempts):
        self.login_attempts += total_attempts
        print("Your login attempt has been recorded")
        print(f"This is attempt number {self.login_attempts}.\n")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Your login attempts counter has been reset to {self.login_attempts}.")


"""Now I have my class, let's make some users"""

user1 = User("Eric", "Bradshaw", "58648", "AzzKicking")
user2 = User("Steve", "Austin", "316", "Rattlesnake")
user3 = User("Stacy", "Keibler", "69696", "PinUp")
user4 = User("Jeff", "Hardy", "489456", "High Flying Cool Brother")

"""Now let's do some stuff with our users"""

user1.full_name()
user1.dept()
user1.greet()
print(user1.login_attempts)
user1.increment_login_attempts(1)
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
user2.full_name()
user2.greet()
user3.full_name()
user3.who()
user3.greet()
user4.full_name()
user4.who()
user4.dept()
user4.greet()

