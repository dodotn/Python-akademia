"""
projekt_2.py: Druhy projekt do Engeto Online Python Akademie

author: Jozef Drga
email: dodo.tn@seznam.cz
"""
import random

def generate_four_digit_number():
    # Generuj prvú cifru (1-9)
    first_digit = random.randint(1, 9)
    # Generuj ďalšie tri cifry (0-9)
    other_digits = [random.randint(0, 9) for _ in range(3)]
    
    # Spoj všetky cifry do jedného čísla
    four_digit_number = f"{first_digit}{other_digits[0]}{other_digits[1]}{other_digits[2]}"
    return four_digit_number

def calculate_bulls_and_cows(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(digit), guess.count(digit)) for digit in set(guess)) - bulls
    return bulls, cows


def pozdrav ():
    print ("Hi there!")
    print (15*"-")
    print ("I've generated a random 4 digit number for you.")
    print ("Let's play a bulls and cows game.")
    print (15*"-")
  

#-----------------------------------------------


def play_game():
    secret_number = generate_four_digit_number()
    attempts = 0

    pozdrav ()

    while True:
        guess = input("Enter a number: ")
        if guess = "q"
           quit()
        if len(guess) != 4 or not guess.isdigit():
            print("Please enter valid, 4 digit number.")
            continue

        attempts += 1
        bulls, cows = calculate_bulls_and_cows(secret_number, guess)
        print (15*"-")
        print(f"Bulls: {bulls}, Cows: {cows}")
        print (15*"-")

        if bulls == 4:
            print(f"Correct, You  geussed the secret number {secret_number} in {attempts} guesses.")
            break

if __name__ == "__main__":
    play_game()