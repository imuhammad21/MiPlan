from cs50 import get_int


def main():
    # Keep prompting user for height of pyramid until they give valid number
    while True:
        height = get_int("Height: ")
        if height >= 0 and height <= 23:
            break
    # In each row, print a specfic number of bricks and spaces that is dependent on the row number
    for i in range(height):
        print(" " * (height - i - 1), end="")
        print("#" * (i + 2))


if __name__ == "__main__":
    main()
