"""
So bored at the dealership getting my oil changed.
Let's make a class about something.
"""

"""First I made my class, since this is what this is all about"""
class Character:
    def __init__(self, char_name, franchise, role):
        self.char_name = char_name
        self.franchise = franchise
        self.role = role

    def myfav(self):
        print(f"You named {self.char_name} when asked.  That must be your favorite ;).")

    def moviefranchise(self):
        print(f"You said this character resided in the {self.franchise} Universe.")

    def characterRole(self):
        print(f"And you said {self.char_name} had the {self.role} in the {self.franchise} Universe.")

prog_out = True # Made this cause I plan to use a loop with some user input

while prog_out: # Here's the start of my loop.
    """Used 'prog_out' as the exit statement of the loop"""

    print("Welcome to my class loop.  Enter 'q' at any time to leave") # Simple greeting
    fav_char = input("What is your favorite character of all time? ") # Character input
    if fav_char == 'q': # Exit clause to leave the loop
        break
    char_fran = input("What franchise is that char part of? ")
    if char_fran == 'q':
        break
    char_role = input("Is the character a Hero or a Villian? ")
    if char_role == 'q':
        break

    abc = Character(fav_char, char_fran, char_role) # Set the input into the class

    """
    Finally I call the class and spit out the input the user gave me from the class
    """

    print("\n")
    abc.myfav()
    abc.moviefranchise()
    abc.characterRole()

"""
I wanted to combine some items on this one.  Take some of what I've learned in other
areas and apply them to a class.  Here is a demonstration of taking a while loop and 
some user input and ran it through a defined Class.
"""
