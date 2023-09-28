# Hash Table

# book = dict()
# book["apple"] = 0.67
# book["milk"] = 1.49
# book["avocado"] = 1.49
# print(book)
# print(book["milk"])


# Implementation of a phone book
# phone_book = {}
# phone_book["mary"] = 912345678
# phone_book["bisi"] = 1900345578
# print(phone_book["bisi"])

# DNS Resolution
# DNS Resolution reflects use case of hash tables
# example of dns resolution is mapping web address to ip address


# Preventing duplicate entries in hash table
# voted = {}
# value = voted.get("tom", 0)


# # Voting System
# voted = {}


# def check_voter(name):
#     if voted.get(name):
#         print("Get out!")
#     else:
#         voted[name] = True
#         print("Let them vote.")


# check_voter("tom")
# check_voter("tom")
# check_voter("Olu")


# # Facebook Cache system
# def get_data_from_server():
#     pass


# cache = {}


# def get_page(url):
#     if cache.get(url):
#         return cache[url]
#     else:
#         data = get_data_from_server(url)
#         cache[url] = data
#         return data
