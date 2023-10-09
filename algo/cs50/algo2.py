# This is an iterating algoritm


def get_height():
    height: int = int(input("Height:"))
    draw(height)


def draw(h):
    for n in range(h):
        for v in range(n + 1):
            print(f"#")


get_height()
