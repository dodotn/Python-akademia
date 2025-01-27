"""
projekt_2.py: Druhy projekt do Engeto Online Python Akademie

author: Jozef Drga
email: dodo.tn@seznam.cz
"""
import random
from typing import Tuple


def generate_four_digit_number() -> str:
    """
    Generates a random 4-digit number where all digits are unique.
    Ensures the first digit is not zero.

    Returns:
        str: A 4-digit number represented as a string.
    """
   
    digits = random.sample(range(10), 4)
    if digits[0] == 0:
        digits[0], digits[1] = digits[1], digits[0]
    four_digit_number = ''.join(map(str, digits))
    return four_digit_number


def calculate_bulls_and_cows(secret: str, guess: str) -> Tuple[int, int]:
    """
    Calculates the number of Bulls (correct digits in the correct position)
    and Cows (correct digits in the wrong position) for a given guess.

    Args:
        secret (str): The secret 4-digit number.
        guess (str): The player's guess.

    Returns:
        Tuple[int, int]: A tuple containing the number of Bulls and Cows.
    """
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(digit), guess.count(digit)) for digit in set(guess)) - bulls
    return bulls, cows


def greeting() -> None:
    """
    Prints a welcome message with the rules of the game.
    """
    print("Hi there!")
    print("-" * 15)
    print("I've generated a random 4-digit number for you.")
    print("Your task is to guess it!")
    print("For every guess, I'll tell you:")
    print(" - Bulls: correct digits in the correct positions")
    print(" - Cows: correct digits in the wrong positions")
    print("Type 'q' anytime to quit the game. The nuber not starts with zero.")
    print("-" * 15)


def play_game() -> None:
    """
    Runs the main game loop. Generates a secret number, takes user input,
    and provides feedback until the user guesses the correct number or quits.

    The user can quit the game by typing 'q'.

    """
    secret_number = generate_four_digit_number()
    attempts = 0

    greeting()

    while True:
        guess = input("Enter a number: ")
        if guess == "q":
            print("Thanks for playing! Goodbye.")
            break
        if len(guess) != 4 or not guess.isdigit():
            print("Please enter a valid 4-digit number.")
            continue
        if guess[0] == '0' and len(guess) > 1:
             print("Number must not start with zero.")
             continue
        
        if len(set(guess)) != 4:
            print("Please enter a number with 4 unique digits.")
            continue

        attempts += 1
        bulls, cows = calculate_bulls_and_cows(secret_number, guess)
        print("-" * 15)
        print(f"Bulls: {bulls}, Cows: {cows}")
        print("-" * 15)

        if bulls == 4:
            print(f"Congratulations! You've guessed the secret number {secret_number} correctly.")
            if attempts == 1:
                print(f"Amazing! You guessed it in just {attempts} try!")
            else:
                print(f"You guessed it in {attempts} tries. Well done!")
            break


if __name__ == "__main__":
    play_game()