class Restaurant:
    """A Restaurant class to be used"""

    def __init__(self, name, cuisine):
        """Defining the __init__ module"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def desc_rest(self):
        print(f"This is {self.name}! A {self.cuisine} restaurant.")

    def open(self):
        print(f"Good morning! {self.name} is now open!")

    def set_number_served(self, served):
        self.number_served = served
        print(f"This restaurant has served {self.number_served} patrons!")

    def increment_served(self, served):
        print(f"{self.name} had served {served}.")
        self.number_served += served
        print(f"{self.name.title()} served {self.number_served} in total after today!")

fav_diner = Restaurant("Fogo De Chow", "Brazillian Steak House")
fav2_diner = Restaurant("Spaghetti Factory", "Italian Pasta")
fav3_diner = Restaurant("Chilli's", "Bar/Grill")

print(f"My favorite place to eat is {fav_diner.name}.")
print(f"{fav_diner.name} is a(n) {fav_diner.cuisine} type of diner.")
print("\n")
fav_diner.desc_rest()
fav_diner.set_number_served(150_759)
fav_diner.increment_served(785)
fav_diner.open()
print("\n")
fav2_diner.desc_rest()
fav2_diner.open()
print("\n")
fav3_diner.desc_rest()
fav3_diner.open()



