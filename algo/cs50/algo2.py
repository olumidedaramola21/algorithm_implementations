# This is an iterating algoritm


def get_height():
    height: int = int(input("Height:"))
    draw(height)


# Recursion is so nice
def draw(h, n=0):
    if h == n:
        return
    row = "#" * (n + 1)
    print(row)
    draw(h, n + 1)


get_height()
