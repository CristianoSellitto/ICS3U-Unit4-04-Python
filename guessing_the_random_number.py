#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in November 2022
# A program that finds if the user's number between 0 and 9 is equal to the random number

import random


def main():
    # Finds if the chosen number from 0 to 9 is equal to the random number

    random_number = random.randint(0, 9)
    try:
        while True:
            chosen_number = input("\nEnter a number from 0 to 9: ")
            chosen_int = int(chosen_number)
            if chosen_int == random_number:
                print("\nYou got the number right!")
                print("The number was {}.".format(random_number))
                break
            elif chosen_int > random_number:
                print("\n{} is higher than the random number.".format(chosen_int))
            elif chosen_int < random_number:
                print("\n{} is lower than the random number.".format(chosen_int))
    except ValueError:
        print("\nThis input isn't an integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
