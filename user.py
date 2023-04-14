class User:
    """A class to define a 'user'"""
    def __init__(self, fname, lname, id, department):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.department = department
        self.login_attempts = 0

    def full_name(self):
        print(f"User's full name is {self.fname} {self.lname}.")

    def who(self):
        print(f"{self.fname}'s ID number is {self.id}.")

    def dept(self):
        print(f"{self.fname} works in the {self.department} department.")

    def greet(self):
        print(f"Welcome {self.fname} {self.lname}!  Good to see you!")
        
    def increment_login_attempts(self, total_attempts):
        self.login_attempts += total_attempts
        print("Your login attempt has been recorded")
        print(f"This is attempt number {self.login_attempts}.")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Your login attempts counter has been reset to {self.login_attempts}.")




"""Now I have my class, let's make some users"""

