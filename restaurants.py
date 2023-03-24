class Restaurant:
    """A Restaurant class to be used"""

    def __init__(self, name, cuisine):
        """Defining the __init__ module"""
        self.name = name
        self.cuisine = cuisine

    def desc_rest(self):
        print(f"This is {self.name}! A {self.cuisine} restaurant.")

    def open(self):
        print(f"Good morning! {self.name} is now open!")

fav_diner = Restaurant("Fogo De Chow", "Brazillian Steak House")
fav2_diner = Restaurant("Spaghetti Factory", "Italian Pasta")
fav3_diner = Restaurant("Chilli's", "Bar/Grill")

print(f"My favorite place to eat is {fav_diner.name}.")
print(f"{fav_diner.name} is a(n) {fav_diner.cuisine} type of diner.")

fav_diner.desc_rest()
fav_diner.open()

fav2_diner.desc_rest()
fav2_diner.open()

fav3_diner.desc_rest()
fav3_diner.open()



