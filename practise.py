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
