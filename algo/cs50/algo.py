def guess():
    numbers = [20, 500, 10, 5, 100, 1, 50]
    n = input("number: ")
    for i in numbers:
        print(i, n)
        if i == int(n):
            print("Found")
            return 0
    print("Not found")
    return 1


guess()
