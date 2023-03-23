class Cat:
    """A simple attempt to model a cat."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting due to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over due to a command"""
        print(f"{self.name} rolled over.")

my_cat = Cat('Benny', 1)
her_cat = Cat('Princess', 1)

print(f"My cat's name is {my_cat.name}.")
print(f"My cat is {my_cat.age} years old.")

my_cat.sit()
my_cat.roll_over()

print(f"Her cat's name is {her_cat.name}.")
print(f"Her cat is {her_cat.age} years old.")

her_cat.sit()
her_cat.roll_over()
