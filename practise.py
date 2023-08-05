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

message = input("Tell me something, and I will repeat it back to you: ")
print(message)
