#!/usr/bin/env python3
# Created by: Adrian student
# Created on: 16th NOV 2026
# This program uses a random number generator to choose a
# random number and then asks the user to try guessing it
import random


def main():
    # set up the random number generator
    number = int(random.randint(0, 9))

    while True:
        # get the user guess number
        user_number_str = input("Enter your guess number between 0 and 9 : ")

        # prevent crashing
        try:
            user_number_int = int(user_number_str)

            # check if the user guess number is in the number interval
            if user_number_int >= 0 and user_number_int <= 9:
                if user_number_int == number:
                    break
                else:
                    print("That is not the correct guess. please try again")
            else:
                print (f"{user_number_int} is off range.")
        except ValueError:
            print(f"{user_number_str} is not an integer")
    print("")
    print("you guessed correctly !!")
    print("Thanks for playing !!")


if __name__ == "__main__":
    main()
