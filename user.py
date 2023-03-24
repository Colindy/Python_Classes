class User:
    """A class to define a 'user'"""
    def __init__(self, fname, lname, id, department):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.department = department

    def full_name(self):
        print(f"User's full name is {self.fname} {self.lname}.")

    def who(self):
        print(f"{self.fname}'s ID number is {self.id}.")

    def dept(self):
        print(f"{self.fname} works in the {self.department}.")

"""Now I have my class, let's make some users"""

user1 = User("Eric", "Bradshaw", "58648", "AzzKicking")
user2 = User("Steve", "Austin", "316", "Rattlesnake")
user3 = User("Stacy", "Keibler", "69696", "PinUp")
user4 = User("Jeff", "Hardy", "489456", "High Flying Cool Brother")

"""Now let's do some stuff with our users"""



