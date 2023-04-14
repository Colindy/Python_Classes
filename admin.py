from user import *

class Privileges:
    def __init__(self, rights = "granted"):
        self.rights = rights

    def show_privileges(self):
        if self.rights == "granted":
            print("You have admin rights")
        else:
            print("You have not been granted rights")

class Admin(User):
    def __init__(self, fname, lname, id, department):
        super().__init__(fname, lname, id, department)
        self.privileges = Privileges()
