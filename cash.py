from cs50 import get_float
import math


def main():
    coins = 0
    while True:
        cash = get_float("How much change? ")
        if cash > 0:
            break
    # Makes the hundreths place now the ones place to perform cleaner subraction
    cash = round(cash * 100)
    # Subract a coin as long as the total value of change is greater than or equal to value of coin
    while cash >= 25:
        coins += 1
        cash -= 25
    while cash >= 10:
        coins += 1
        cash -= 10
    while cash >= 5:
        coins += 1
        cash -= 5
    # When you only have pennies left, number of coins necessary = number of pennies, so you can add this to the counter
    coins += cash

    print(f"Total Coins: {coins}")


if __name__ == "__main__":
    main()
