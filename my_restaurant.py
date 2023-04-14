from restaurants import Restaurant

name = input("What's your favorite Restaurants name? ")
cuisine = input("Right on!  What type of food do they serve? ")

my_fav = Restaurant(name, cuisine)

my_fav.desc_rest()
