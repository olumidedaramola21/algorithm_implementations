# message = "Hello!"
# print(message)

# firstName = "olumide"
# print("Hello " + firstName.title() + ", would you like to learn some python today!")
# print(4 // 2)
# print(4 / 2)
# print(9 / 2)
# print(9 // 2)
# favorite_number = 14
# print("My Favorite number is: " + str(favorite_number))

# LISTS
# bicycles = ["trek", "cannondale", "redline", "specialized"]
# print(bicycles)
# print(bicycles[0])
# print(bicycles[3])
# print(bicycles[len(bicycles)])
# friends = ["timi", "olumide", "anana"]
# print("My best friend is " + friends[0])
# print("This is my childhood friend " + friends[1])
# motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
# # last_owned = motorcycles.pop()
# # print("The last motorcycle i owned was a " + last_owned + ".")
# too_expensive = "ducati"
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print("A " + too_expensive.title() + " is too expensive for me.")


# list = ["cr7", "messi", "rooney", "snachez"]
# print("I invite to my meeting " + list[0])
# print("I invite to my meeting " + list[1])
# print("I invite to my meeting " + list[2])
# print(list[2] + " could not attend my meeting.")
# list[2] = "rashford"
# print("I invite to my meeting " + list[0])
# print("I invite to my meeting " + list[1])
# print("I invite to my meeting " + list[2])
# print("I have found a bigger dinner table.")

# mid = len(list) // 2

# list.insert(0, "mbappe")
# list.insert(mid, "bruno")
# list.append("hakimi")

# print(list)

# cars = ["bmw", "audi", "toyota", "subaru"]
# cars.sort()
# print(cars)

# places = ["lisbob", "london", "san-francisco", "new-york", "austria"]
# print(places)
# isorted = sorted(places)
# print(isorted)
# print(places)
# places.reverse()
# print(places)
# places.reverse()
# places.sort()
# places.sort(reverse=True)

# list = [2, 4, 1, 3, 6, 7, 9, 1]
# list.sort()
# print(list)

# magicians = ["alice", "david", "carolina"]
# for magician in magicians:
#     print(magician.title() + ", that was a great trick!")
#     print("I can't wait to see your next trick, " + magician.title() + ".\n")

# food_stuff = ["rice", "yam", "beans"]
# for food in food_stuff:
#     print("I like " + food)

# print("I really pizza.")

# squares = []
# for value in range(1, 11):
#     square = value**2
#     squares.append(square)

# print(squares)
# for value in range(1, 21):
#     print(value)
# for odd_num in range(1, 20, 3):
#     print(odd_num)

# cubed = [value**3 for value in range(1, 11)]
# print(cubed)
# # for value in range(1, 11):
# #     cube = value**3
# #     cubed.append(cube)
# # print(cubed)

# players = ["charles", "martina", "michael", "florence", "eli"]
# print(players[-3:])

# foods = ("bread", "rice", "yam", "beans")
# foods[0] = "yam2"
# for food in foods:
#     print(food)

# car = "subaru"
# print("Is car == 'subaru'? I predict True.")
# print(car == "subaru")

# age = 12

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# else:
#     price = 10
# print("Your admission cost is " + str(price) + ".")

# alien_color = "red"
# if alien_color == "green":
#     print("player just earned 5 points.")
# else:
#     print("player just added 10points")

# if alien_color == "red":
#     print("player just earned 5 points")
# if alien_color == "green":
#     print("player just earned 10 points")

# available_toppings = [
#     "mushrooms",
#     "olives",
#     "green peppers",
#     "pepperoni",
#     "pineapple",
#     "extra cheese",
# ]
# requested_toppings = ["mushrooms", "french fries", "extra cheese"]
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print("Adding " + requested_topping + ".")
#     else:
#         print("Sorry, we don't have " + requested_topping + ".")


#  HELLO ADMIN ######## AND NO USERS
# user_name = ["admin", "clock", "time", "nigeria", "mouse"]
# # user_name = []

# if len(user_name) == 0:
#     print("We need to find some users!")
# else:
#     for user in user_name:
#         if user == "admin":
#             print("Hello " + user + ", would you like to see a status report?")
#         else:
#             print("Hello " + user + ", thank you for logging in again.")


# #  ##########CHECKING USERNAME#########
# current_users = [
#     "abc@gmail.com",
#     "bac@gmail.com",
#     "cab@gmail.com",
#     "acb@gmail.com",
#     "bca@gmail.com",
# ]
# new_users = [
#     "def@gmail.com",
#     "efd@gmail.com",
#     "cab@gmail.com",
#     "abc@gmail.com",
#     "fed@gmail.com",
# ]
# for new in new_users:
#     if new.lower() in (current.lower() for current in current_users):
#         print
#         print("Username " + new + " already exits, enter a new username!")
#     else:
#         print("Username is avaible")


# ########################ORDINAL NUMBERS######################
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for num in numbers:
#     if num == 1:
#         print(str(num) + "st")
#     elif num == 2:
#         print(str(num) + "nd")
#     elif num == 3:
#         print(str(num) + "rd")
#     else:
#         print(str(num) + "th")

# ##########################DICTIONARIES###################

# # ##########################ALIEN SPEED
# alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
# print("Original x-position: " + str(alien_0["x_position"]))
# alien_0["speed"] = "old"

# if alien_0["speed"] == "slow":
#     x_increment = 1
# elif alien_0["speed"] == "medium":
#     x_increment = 2
# else:
#     x_increment = 3

# alien_0["x_position"] = alien_0["x_position"] + x_increment

# print("New x-position: " + str(alien_0["x_position"]))


# favorite_programming = {"olumide": "python", "ade": "javascript", "femi": "c++"}

# Olumide_information = {
#     "first_name": "olumide",
#     "last_name": "Daramola",
#     "age": 21,
#     "city": "akure",
# }

# for k, v in Olumide_information.items():
#     print("\nK: " + k)
#     print("V: " + str(v))

# favorite_languages = {"jen": "python", "sarah": "c", "edward": "ruby", "phil": "python"}

# friends = ["phil", "sarah"]
# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#         print(
#             " Hi "
#             + name.title()
#             + ", I see your favorite language is "
#             + favorite_languages[name].title()
#             + "!"
#         )

#  #########RIVERS###########
# rivers = {"nile": "egypt", "yello": "china", "amazon": "south-america"}

# for key, value in rivers.items():
#     print("The " + key + " runs through " + value + ".")
#     for key in rivers.keys():
#         print(key)
#     for value in rivers.values():
#         print(value)

# ############POLING##############
# favorite_languages = {"jen": "python", "sarah": "c", "edward": "ruby", "phil": "python"}

# friends = ["phil", "sarah", "miracle"]

# for friend in friends:
#     if friend not in favorite_languages.keys():
#         print("I invite you to take the poll " + friend + ".")
#     else:
#         print("Thanky you for responding " + friend + ".")

# #############
# print(range(5))
# for value in range(5):
#     print(value)

#

# NESTING #

# alien_0 = {"color": "green", "points": 5}
# alien_1 = {"color": "yello", "points": 10}
# alien_2 = {"color": "red", "points": 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# pizza = {"crust": "thick", "toppings": ["mushrooms", "extra cheese"]}

# print(
#     "You ordered a " + pizza["crust"] + "-crust pizza " + "with the following toppings:"
# )

# for topping in pizza["toppings"]:
#     print("\t" + topping)

# favorite_languages = {
#     "jen": ["python", "ruby"],
#     "sarah": ["c"],
#     "edward": ["ruby", "go"],
#     "phil": ["python", "haskell"],
# }

# for name, languages in favorite_languages.items():
#     if len(languages) > 1:
#         print("\n" + name.title() + "'s favorite languages are:")
#         for language in languages:
#             print("\t" + language.title())
#     else:
#         print("\n" + name.title() + " favorite languages is: ")
#         print("\t" + language.title())

# users = {
#     "aienstein": {
#         "first": "albert",
#         "last": "einstein",
#         "location": "princeton",
#     },
#     "mcurie": {
#         "first": "marie",
#         "last": "curie",
#         "location": "paris",
#     },
# }

# for username, user_info in users.items():
#     print("\nUsername: " + username)
#     full_name = user_info["first"] + " " + user_info["last"]
#     location = user_info["location"]

#     print("\tFull name: " + full_name.title())
#     print("\tLocation: " + location.title())

# PEOPLE EXample
# Olumide_information = {
#     "first_name": "olumide",
#     "last_name": "Daramola",
#     "age": 21,
#     "city": "akure",
# }

# Ade_information = {
#     "first_name": "ade",
#     "last_name": "Dola",
#     "age": 25,
#     "city": "lagos",
# }

# Ola_information = {
#     "first_name": "ola",
#     "last_name": "Olu",
#     "age": 26,
#     "city": "abuja",
# }


# people = [Olumide_information, Ade_information, Ola_information]
# for person in people:
#     print("This is the everything i know about them: ")
#     Full_name = person["first_name"] + " " + person["last_name"]
#     location = person["city"]
#     age = person["age"]

#     print(
#         "\tTheir full_name is: "
#         + Full_name.title()
#         + ",city: "
#         + location.title()
#         + ", age: "
#         + str(age)
#     )

# layke = {"type": "dog", "owner": "mr a"}

# jack = {"type": "dog", "owner": "mr b"}

# pets = [layke, jack]

# for pet in pets:
#     print(pet["type"], pet["owner"])

# favorite_places = {
#     "olumide": ["new york", "san_franciso"],
#     "ade": ["lisbon", "lagos"],
#     "ola": ["london", "aba"],
# }

# for name, favorite_place in favorite_places.items():
#     print(name + "'s favorite_places are: ")
#     for place in favorite_place:
#         print("\t " + place)
# # for place in favorite_place:


# FAVORITE NUMBER
# favorite_number = {
#     "olumide": [14, 13, 12, 11],
#     "peter": [12, 14, 16, 18],
#     "israel": [13, 16, 19, 22],
#     "ade": [15, 17, 19, 21],
#     "jpaul": [176, 177, 189, 98],
# }

# for name, numbers in favorite_number.items():
#     print(name + " favorite_numbers are: ")
#     for number in numbers:
#         print([str(number)])

# CITIES. print the name of each city and all of the information stored in them.
# cities = {
#     "lagos": {
#         "country": "Nigeria",
#         "population": 140000,
#         "Key_fact": "Nigeria is the most populous country in Africa",
#     },
#     "lisbon": {
#         "country": "Portugal",
#         "population": 10000,
#         "Key_fact": "Lisbon is the second smallest city in europe.",
#     },
#     "Berlin": {
#         "country": "Germany",
#         "population": 8000,
#         "Key_fact": "Berlin is the oil capital of the world0",
#     },
# }

# for city, city_info in cities.items():
#     print("Today we are considering: " + city)
#     for k, info in city_info.items():
#         print("\t" + k + ": " + str(info))

# Extension

# INPUT

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# current_number = 1

# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# prompt = "\nTell me something, and i will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# message = ""
# active = True

# while active:
#     message = input(prompt)

#     if message == "quit":
#         active = False
#     else:
#         print(message)

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"

# while True:
#     city = input(prompt)

#     if city == "quit":
#         break
#     else:
#         print("I'd love  to go to " + city.title() + "!")

# USING CONTINUE
# current_number = 0
# while current_number < 10:
#     current_number += 1

#     if current_number % 2 == 0:
#         continue

#     print(current_number)

# PIZZA TOPPINGS
# prompt = "\nPlease, Enter your favorite topping:"
# prompt += "\nenter 'quit' to  exit."

# active = True

# while active:
#     message = input(prompt)

#     if message == "quit":
#         break
#     else:
#         print(message + " will be added to pizza.")

# MOVIE TICKETS
# prompt = "\nPlease, enter your age (or 'quit' to end program):"

# message = ""

# active = True

# while active:
#     message = input(prompt)

#     if message.isdigit():
#         age = int(message)

#         if age < 3:
#             print("The cost of your movie ticket is Free")
#         elif 3 <= age <= 12:
#             print("The cost of your movie ticket is $" + str(10))
#         else:
#             print("The cost of your movie ticket is $" + str(15))

#     elif message == "quit":
#         print("Goodbye")
#         break
#     else:
#         print("Invalid input. Please enter a valid age or 'quit'")

# Start with users that need  to be verified
# and an empty list to hold confirmed users.

# unconfirmed_users = ["alice", "brian", "candace"]
# confirmed_users = []

# # Verify each user until there are no more uncofirmed users.
# # Move each verified user into the list of confirmed users.

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)

#     # Display all confirmed users.
#     print("\nThe following users have been confirmed:")
#     for confirmed_user in confirmed_users:
#         print(confirmed_user.title())

# pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
# print(pets)

# while "cat" in pets:
#     pets.remove("cat")

#     print(pets)

# POLLING PROGRAM
# reponses = {}
# # set a flag to indicate that polling is active
# polling_active = True

# while polling_active:
#     # Prompt for the person's name and response.
#     name = input("\nWhat is your name?")
#     reponse = input("Which mountain would you like to climb ")

#     # store the response in the dictionary
#     reponses[name] = reponse
#     # Find out if any one else is taking poll
#     repeat = input("Would you like to let another person respond?(Yes/No)")
#     if repeat == "No":
#         polling_active = False

# # Polling is complete. Show the results.
# print("\n--- Poll Results---")
# for name, response in reponses.items():
#     print(name + " would like to climb " + response + ".")

# sandwich_orders = [
#     "pastrami",
#     "sandwich_a",
#     "pastrami",
#     "sandwish_b",
#     "pastrami",
#     "sandwish_c",
#     "pastrami",
#     "pastrami",
# ]
# finished_sandwiches = []

# while sandwich_orders:
#     print("deli has run out of pastrami")

#     while "pastrami" in sandwich_orders:
#         sandwich_orders.remove("pastrami")

#     sandwich = sandwich_orders.pop()
#     print("I made your " + sandwich)

#     finished_sandwiches.append(sandwich)

# for sandwich in finished_sandwiches:
#     print(sandwich + " has been made.")


# # POLLING PROGRAM 1 AND POLLING PROGAM 2
# # reponses = {}
# reponses = {}
# # # set a flag to indicate that polling is active
# # polling_active = True
# polling_active = True

# # while polling_active:
# while polling_active:
#     #     # Prompt for the person's name and response.
#     #     name = input("\nWhat is your name?")
#     name = input("\nWhat is your name?")
#     #     reponse = input("Which mountain would you like to climb ")
#     question = input("\nIf you could visit one place in the world, where would you go?")

#     #     # store the response in the dictionary
#     #     reponses[name] = reponse
#     reponses[name] = question
#     # Find out if any one else is taking poll
#     repeat = input("Would you like to let another person respond?(Yes/No)")
#     if repeat == "No":
#         polling_active = False

# # Polling is complete. Show the results.
# print("\n--- Poll Results---")
# for name, question in reponses.items():
#     print(name + " would love to visit " + question + ".")


# FUNCTIONS
# def greet_user(username):
#     """Display a simple greeting"""
#     print("Hello, " + username + "!")


# greet_user("Jesse")


# def display_message():
#     print("I Love Jesus!")


# display_message()


# def favorite_book(title):
#     print("One of my favorite books is " + title + ".")


# favorite_book("Alice in wonderland")


# def describe_pet(animal_type, pet_name):
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# describe_pet("Hamster", "harry")
# describe_pet("dog", "willie")


# def make_shirt(size="large", message="I love python"):
#     print("My shirt is a size " + size)
#     print("I want this message printed on it: " + message)


# make_shirt("medium", "I want to become a software developer.")
# make_shirt()
# make_shirt("small")


#


# def build_person(first_name, last_name, age=""):
#     person = {"first": first_name, "last": last_name}
#     if age:
#         person["age"] = age
#     return person

#     return person


# musician = build_person("jimi", "hendrix", age=27)
# print(musician)


# def get_formatted_name(first_name, last_name):
#     full_name = first_name + " " + last_name
#     return full_name


# is_active = True

# while is_active:
#     print("\nPlease tell me your name: ")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("first_name: ")
#     if f_name == "q":
#         break
#     l_name = input("last_name: ")
#     if l_name == "q":
#         break

#     formated_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formated_name + "!")


# def city_country(city_name, country_name):
#     formatted_city_country = city_name + ", " + country_name
#     return formatted_city_country


# a = city_country("Santiago", "Chile")
# b = city_country("Lisbon", "Portugal")
# c = city_country("Lagos", "Nigeria")
# print(a, b, c)


# def make_album(arstist_name, album_title, number_of_tracks=""):
#     if number_of_tracks:
#         album = {
#             "Arstist_name": arstist_name,
#             "album_title": album_title,
#             "number of tracks": number_of_tracks,
#         }
#     else:
#         album = {"Arstist_name": arstist_name, "album_title": album_title}
#     return album


# while True:
#     print("\nPlease give arstist_name, album_title: ")
#     print("(enter 'q' at any time to quit)")
#     a_name = input("arstist_name: ")
#     if a_name == "q":
#         break
#     a_title = input("album_title: ")
#     if a_title == "q":
#         break

#     arstist = make_album(a_name, a_title)
#     print(arstist)

#     formated_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formated_name + "!")

# olamide = make_album("Olamide", "unruly", 14)
# wizkid = make_album("Wizkid", "essense")
# burnaboy = make_album("burnaboy", "dangote")

# print(olamide)
# print(burnaboy)
# print(wizkid)


# def greet_users(names):
#     for name in names:         msg = "Hello, " + name.title() + "!"
#         print(msg)


# usernames = ["hannah", "ty", "margot"]
# greet_users(usernames)

# magicians_names = ["olu", "ade", "bayo", "eazi"]


# def show_magicians(names):
#     for name in names:
#         print(name)


# def make_great(names):
#     new_list = []
#     for name in names:
#         new_list.append("Great " + name)
#     return new_list


# modified_names = make_great(magicians_names[:])
# show_magicians(magicians_names)
# show_magicians(modified_names)


# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print("-" + topping)


# make_pizza("pepperoni")
# make_pizza("mushrooms", "green peppers", "extra cheese")


# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make"""
#     print("Making a " + str(size) + "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("-" + topping)


# make_pizza(16, "pepperoni")
# make_pizza(12, "mushrooms", "green peppers", "extra cheese")


# Class


# class Dog():
#     """A simple attempt to model a dog."""

#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(self.name.title() + " is now sitting.")

#     def roll_over(self):
#         """Simulate a dog rolling over in response to a command."""
#         print(self.name.title() + " rolled over!")


# my_dog = Dog("willie", 6)
# my_dog.sit()
# my_dog.roll_over()

# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog's age is " + str(my_dog.age) + ".")


# Class example one: Restaurant
# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(self.restaurant_name.title() + " is the best restaurant in Nigeria")
#         print(
#             self.restaurant_name.title()
#             + " serves this type of cuisine "
#             + self.cuisine_type
#         )

#     def open_restaurant(self):
#         print("We are open")


# restaurant1 = Restaurant("aba", "hot_meal")
# restaurant2 = Restaurant("aba", "hot_meal")
# restaurant3 = Restaurant("aba", "hot_meal")

# restaurant1.open_restaurant()
# restaurant1.describe_restaurant()
# restaurant2.open_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.open_restaurant()
# restaurant3.describe_restaurant()

# USers


# class Users:
#     def __init__(self, first_name, last_name, age, nationality):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.nationality = nationality
#         self.login_attempts = 0

#     def describe_user(self):
#         print(
#             "My name is "
#             + self.first_name
#             + " "
#             + self.last_name
#             + ", I'm "
#             + str(self.age)
#             + " and i'm a citizen of "
#             + self.nationality
#         )

#     def greet_user(self):
#         print("Hello " + self.first_name + "!")

#     def increment_login_attempts(self):
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         self.login_attempts = 0

#     def print_login_attempts(self):
#         print(self.login_attempts)


# first_user = Users("Olumide", "Daramola", 21, "Nigerian")
# first_user.increment_login_attempts()
# first_user.increment_login_attempts()
# first_user.increment_login_attempts()
# first_user.increment_login_attempts()
# first_user.print_login_attempts()
# first_user.reset_login_attempts()
# first_user.print_login_attempts()

# first_user.describe_user()
# first_user.greet_user()
# second_user = Users("Omobolaji", "Daramola", 23, "Nigerian")
# second_user.describe_user()
# second_user.greet_user()
# third_user = Users("Israel", "Adenigba", 19, "Nigerian")
# third_user.describe_user()
# third_user.greet_user()

# Testing The NONE Return
# def foo1(value):
#     if value:
#         return value
#     else:
#         return None


# def foo2(value):
#     if value:
#         return value
#     else:
#         return


# def foo3(value):
#     if value:
#         return value


# print(foo1(0))
# print(foo2(0))
# print(foo3(0))


# class Car:
#     # A simple attempt to represent a car
#     def __init__(self, make, model, year):
#         # Initialize attributes to describe a car
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         # Return a neatly formatted descriptive name
#         long_name = str(self.year) + " " + self.make + " " + self.model
#         return long_name.title()

#     def read_odometer(self):
#         # print a statement showing car mileage
#         print("This car has " + str(self.odometer_reading) + " miles on it")

#     def update_odometer(self, mileage):
#         # set the odometer reading to the given value
#         if mileage > self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back on odometer")

#     def increment_odometer(self, miles):
#         # Add the given amount to the odometer reading
#         if miles > 0:
#             self.odometer_reading += miles


# my_used_car = Car("Subaru", "outback", 2013)
# print(my_used_car.get_descriptive_name())
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

# 9_4 Numbers served


# Class example one: Restaurant
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         print(self.restaurant_name.title() + " is the best restaurant in Nigeria")
#         print(
#             self.restaurant_name.title()
#             + " serves this type of cuisine "
#             + self.cuisine_type
#             + " and this is the number of people already served at the party: "
#             + str(self.number_served)
#         )

#     def set_number_served(self, number):
#         self.number_served = number

#     def increment_number_served(self, number):
#         self.number_served += number


# restaurant1 = Restaurant("aba", "hot_meal")
# # restaurant1.number_served = 12
# # restaurant1.set_number_served(15)
# restaurant1.increment_number_served(23)
# restaurant1.describe_restaurant()


# class Car:
#     # A simple attempt to represent a car
#     def __init__(self, make, model, year):
#         # Initialize attributes to describe a car
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         # Return a neatly formatted descriptive name
#         long_name = str(self.year) + " " + self.make + " " + self.model
#         return long_name.title()

#     def read_odometer(self):
#         # print a statement showing car mileage
#         print("This car has " + str(self.odometer_reading) + " miles on it")

#     def update_odometer(self, mileage):
#         # set the odometer reading to the given value
#         if mileage > self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back on odometer")

#     def increment_odometer(self, miles):
#         # Add the given amount to the odometer reading
#         if miles > 0:
#             self.odometer_reading += miles

#     def fill_gas_tank(self):
#         # print that all cars need to fill gas tank
#         print("Fill your gas tank")


# class ElectricCar(Car):
#     # Represent aspects of car, specific to electric vehicles

#     def __init__(self, make, model, year):
#         # Initialize attributes of the parent class.
#         # Then initialize attributes specific to an electric car
#         super().__init__(make, model, year)
#         self.battery_size = 70
#         self.battery = Battery()

#     def fill_gas_tank(self):
#         # Override the parent class
#         print("Electric cars do not need fuel")


# class Battery:
#     # A simple attempt to model a battery for an electric car

#     def __init__(self, battery_size=70):
#         # Initialize the battery's attributes
#         self.battery_size = battery_size

#     def describe_battery(self):
#         # Print a statement describing the battery size.
#         print("This car has a " + str(self.battery_size) + "-KWh battery.")

#     def get_range(self):
#         # Print a statement about the range this battery provides.
#         if self.battery_size == 70:
#             range = 240
#         else:
#             range = 270

#         message = "This car can go approximately " + str(range)
#         message += " miles on a full charge."
#         print(message)


# my_telsa = ElectricCar("tesla", "model s", 2016)
# # print(my_telsa.get_descriptive_name())
# my_telsa.battery.describe_battery()
# my_telsa.battery.get_range()
# # print(str(my_telsa.battery_size))


# ICE CREAM STAND

# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         print(self.restaurant_name.title() + " is the best restaurant in Nigeria")
#         print(
#             self.restaurant_name.title()
#             + " serves this type of cuisine "
#             + self.cuisine_type
#             + " and this is the number of people already served at the party: "
#             + str(self.number_served)
#         )

#     def set_number_served(self, number):
#         self.number_served = number

#     def increment_number_served(self, number):
#         self.number_served += number


# class IceCreamStand(Restaurant):
#     # This class will extend the restaurant class

#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = ["vanilla", "chocolate", "strawberry", "apple"]

#     def display_flavors(self):
#         # This prints out the flavors
#         print(self.flavors[0])


# my_icream_stand = IceCreamStand("abe's ice_cream", "icecream")
# my_icream_stand.display_flavors()


# ADMIN

# class Users:
#     def __init__(self, first_name, last_name, age, nationality):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.nationality = nationality
#         self.login_attempts = 0

#     def describe_user(self):
#         print(
#             "My name is "
#             + self.first_name
#             + " "
#             + self.last_name
#             + ", I'm "
#             + str(self.age)
#             + " and i'm a citizen of "
#             + self.nationality
#         )

#     def greet_user(self):
#         print("Hello " + self.first_name + "!")

#     def increment_login_attempts(self):
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         self.login_attempts = 0

#     def print_login_attempts(self):
#         print(self.login_attempts)


# class Admin(Users):
#     # This class extends the class of Users
#     def __init__(self, first_name, last_name, age, nationality):
#         super().__init__(first_name, last_name, age, nationality)
#         self.privileges = ["can add post", "can delete post", "can ban users"]

#     def show_privileges(self):
#         # This function list the admin privileges
#         print(
#             "This are the admin's privileges: "
#             + "\n"
#             + self.privileges[0]
#             + "\n"
#             + self.privileges[1]
#             + "\n"
#             + self.privileges[2]
#         )


# olumide = Admin("Olumide", "Daramola", 21, "Nigeria")
# olumide.show_privileges()


# BATTERY UPGRADE
# class Car:
#     # A simple attempt to represent a car
#     def __init__(self, make, model, year):
#         # Initialize attributes to describe a car
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         # Return a neatly formatted descriptive name
#         long_name = str(self.year) + " " + self.make + " " + self.model
#         return long_name.title()

#     def read_odometer(self):
#         # print a statement showing car mileage
#         print("This car has " + str(self.odometer_reading) + " miles on it")

#     def update_odometer(self, mileage):
#         # set the odometer reading to the given value
#         if mileage > self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back on odometer")

#     def increment_odometer(self, miles):
#         # Add the given amount to the odometer reading
#         if miles > 0:
#             self.odometer_reading += miles

#     def fill_gas_tank(self):
#         # print that all cars need to fill gas tank
#         print("Fill your gas tank")


# class ElectricCar(Car):
#     # Represent aspects of car, specific to electric vehicles

#     def __init__(self, make, model, year):
#         # Initialize attributes of the parent class.
#         # Then initialize attributes specific to an electric car
#         super().__init__(make, model, year)
#         self.battery_size = 70
#         self.battery = Battery()

#     def fill_gas_tank(self):
#         # Override the parent class
#         print("Electric cars do not need fuel")


# class Battery:
#     # A simple attempt to model a battery for an electric car

#     def __init__(self, battery_size=70):
#         # Initialize the battery's attributes
#         self.battery_size = battery_size

#     def describe_battery(self):
#         # Print a statement describing the battery size.
#         print("This car has a " + str(self.battery_size) + "-KWh battery.")

#     def get_range(self):
#         # Print a statement about the range this battery provides.
#         if self.battery_size == 70:
#             range = 240
#         else:
#             range = 270

#         message = "This car can go approximately " + str(range)
#         message += " miles on a full charge."
#         print(message)

#     def upgrade_battery(self):
#         # Checks the battery size
#         if self.battery_size != 85:
#             self.battery_size = 85


# my_telsa = ElectricCar("tesla", "model s", 2016)
# my_telsa.battery.describe_battery()
# my_telsa.battery.get_range()
# my_telsa.battery.upgrade_battery()
# # my_telsa.battery.get_range()


# ERROR HANDLING
# print(5 / 0) --> ZeroDivisionError
# try:
#     print(5 / 0)
# except ZeroDivisionError:
#     print("Division by zero is not allowed")

# division.py
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit")

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == "q":
#         break
#     second_number = input("Second number: ")
#     if second_number == "q":
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0")
#     else:
#         print(answer)

char_count = [0] * 26
print(char_count)
