def guess():
    strings = ["battleship", "boot", "cannon", "iron", "thimble", "top hat"]

    try:
        n = input("string: ")
    except ValueError:
        print("Invalid input, Please put a valid input")

    for i in strings:
        if i == n:
            print("Found")
            return 0
    print("Not found")
    return 1


guess()
