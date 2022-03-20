# Script written by Peyton Sparks on 03/20/2022
# This script aims to collect user input and then
# use the responses to generate a password for the user

import random


def main():
    # Loop to ensure program doesn't exit until user says so
    while True:
        # Dictionary containing possible characters for password inclusion
        AllCharacters = {
            # Capital letters
            1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F',
            7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L',
            13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R',
            19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X',
            25: 'Y', 26: 'Z',

            # Lowercase letters
            27: 'a', 28: 'b', 29: 'c', 30: 'd', 31: 'e', 32: 'f',
            33: 'g', 34: 'h', 35: 'i', 36: 'j', 37: 'k', 38: 'l',
            39: 'm', 40: 'n', 41: 'o', 42: 'p', 43: 'q', 44: 'r',
            45: 's', 46: 't', 47: 'u', 48: 'v', 49: 'w', 50: 'x',
            51: 'y', 52: 'z',

            # Special characters
            53: '!', 54: '\"', 55: '#', 56: '$', 57: '%', 58: '&',
            59: '\'', 60: '(', 61: ')', 62: '*', 63: '+', 64: ',',
            65: '-', 66: ".", 67: '/', 68: ':', 69: ';', 70: '<',
            71: '>', 72: '=', 73: '?', 74: '@', 75: '[', 76: ']',
            77: '^', 78: '_', 79: '-', 80: '`', 81: '{', 82: '}',
            83: '|', 84: '\\', 85: '~',

            # Numbers
            86: '0', 87: '1', 88: '2', 89: '3', 90: '4', 91: '5',
            92: '6', 93: '7', 94: '8', 95: '9'
        }

        # Variable will house the end result for the random password
        FinalVal = ''

        # Counter for password length iteration lines 99 - 131
        i = 1

        # Title bar
        print('|-------------------------------------------------------------------| \n'
              '|                                                                   | \n'
              '|                     Password Generation Script                    | \n'
              '|                                                                   | \n'
              '|-------------------------------------------------------------------| \n')

        # Collect user input for how password length, try to convert to int
        while True:
            # Collect user input
            Length = input(" How many characters would you like in your password? 1 - 40 ")

            # Try to convert input to int
            try:
                Length = int(Length)
            # Tell user to retry input
            except ValueError:
                print(" Input not valid, please enter a number")

            # Check to ensure length is valid and break if so. Length could be
            # made larger, but it isn't feasible for password entry to do so
            if Length <= 0 or Length > 40:
                print(" Input not valid, please enter a number between 1 - 40")
            else:
                break

        # Collect user input for if a special character should be included, then check for valid input
        while True:
            # Collect user input
            UseSpecChar = input(" Would you like to include special characters? Y/N ")
            UseSpecChar = UseSpecChar.upper()

            # Confirm user input valid then break while loop if valid
            if UseSpecChar not in ('Y', 'N'):
                print(" Input not valid, please try again using Y or N as input...")
            # Break from loop
            else:
                break

        # Collect user input for if a number should be included, then check for valid input
        while True:
            # Collect user input
            UseNumber = input(" Would you like to include numbers? Y/N ")
            UseNumber = UseNumber.upper()

            # Confirm user input valid then break while loop if valid
            if UseNumber not in ('Y', 'N'):
                print(" Input not valid, please try again using Y or N as input...")

            # Break from loop
            else:
                break

        # Both special characters and numbers allowed
        if UseSpecChar == 'Y' and UseNumber == 'Y':
            while i <= Length:
                RandomVal = random.randint(1, 95)

                FinalVal += AllCharacters[RandomVal]
                i += 1

        # Special characters allowed but not numbers
        elif UseSpecChar == 'Y' and UseNumber == 'N':
            while i <= Length:
                RandomVal = random.randint(1, 85)

                FinalVal += AllCharacters[RandomVal]
                i += 1

        # Numbers allowed but not special characters
        elif UseSpecChar == 'N' and UseNumber == 'Y':
            while i <= Length:
                RandomChar = random.randint(1, 52)
                RandomSpecChar = random.randrange(86, 95)
                RandomVal = random.choice((RandomChar, RandomSpecChar))

                FinalVal += AllCharacters[RandomVal]
                i += 1

        # Neither special characters nor numbers allowed
        else:
            while i <= Length:
                RandomVal = random.randint(1, 52)

                FinalVal += AllCharacters[RandomVal]
                i += 1

        # Print generated password
        print(' Generated Password:', "\033[4m" + FinalVal + "\033[0m")

        # Check if user wants to enter a new password
        Continue = input(' Would you like to generate another password? Y/N')
        Continue = Continue.upper()

        # Break from final while loop if user enters anything other than Y
        if Continue != "Y":
            print('\n Thank you for using my password generator! \n')
            break


# Runs main function
if __name__ == '__main__':
    main()
