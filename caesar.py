import cs50
import sys


def main():
    alphalen = 26
    # If python caesar.py is not followed by 1 other string, ask the user to do so and quit program
    if len(sys.argv) != 2:
        print("Enter 1 integer after caesar.py")
        exit(1)
    key = int(sys.argv[1])
    # Acquire plaintext from user
    plaintext = cs50.get_string("Plaintext: ")
    print("ciphertext: ", end="")
    length = len(plaintext)
    for i in plaintext:
        # If character is alphabetic, convert to alphabetical index, add key, convert back, and print
        if i.isalpha():
            if i.isupper():
                letter = ord(i) - ord('A')
                i = (letter + (key)) % alphalen + ord('A')
            elif i.islower():
                letter = ord(i) - ord('a')
                i = (letter + (key)) % alphalen + ord('a')
            print(chr(i), end="")
        # If character is not alphabetic, then simply print
        else:
            print(i, end="")
    print()


if __name__ == "__main__":
    main()
