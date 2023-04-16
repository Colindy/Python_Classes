from random import randint, choice



while True:
    dice = randint(1, 6)
    print(f"You rolled a {dice}!")

    if dice == 3:
        break

while True:
    dice = randint(1, 20)
    print(f"You rolled a {dice}!")

    if dice == 13:
        break

my_ticket = 453167
counter = 0

# Create a loop to count iterations for how long it takes a random number to match my_ticket

while True:
    winning_ticket = randint(1, 999999)

    if winning_ticket != my_ticket:
        counter += 1
    else:
        print(f"Your ticket was matched!  It only took {counter} times to get it!")
        break


"""
This one took a bit.  Had to move the counter outside of the loop because it kept kicking back
as 1 time.  I realized after printing the winning ticket each time in the loop that the counter
kept resetting to 0 if the winning_ticket didn't match my_ticket.  But is working correctly now.

I may have made a rookie mistake and initially made my_ticket a string.....DOH!!  <3 infinite loops....
"""