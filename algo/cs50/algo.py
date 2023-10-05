def guess():
    numbers = [20, 500, 10, 5, 100, 1, 50]

    try:
        n = int(input("number: "))
    except ValueError:
        print("Invalid input, Please put a valid input")

    for i in numbers:
        if i == n:
            print("Found")
            return 0
    print("Not found")
    return 1


guess()
