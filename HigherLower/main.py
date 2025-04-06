# TODO: import system and name from os
from os import system, name

# TODO: import random
import random

# TODO: import logo from art
from art import logo

# TODO: import vs from art
from art import vs

# TODO: import data from game_data
from game_data import data

# TODO: define a clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def format_data(celebrity):
    """Takes the celebrity data and returns the printable format."""
    name = celebrity['name']
    description = celebrity['description']
    country = celebrity['country']
    return f"{name}, a {description}, from {country}"

# TODO: create a function that compares both comparison elements
def compare(first_celebrity, second_celebrity):
    if first_celebrity["follower_count"] > second_celebrity["follower_count"] :
        return "A"
    else:
        return "B"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess et follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# TODO: create a score variable
score = 0

game_should_continue = True

second_celebrity = random.choice(data)

# TODO: print the logo
print(logo)

# TODO: create a play_game function
while game_should_continue:
    clear()

    # TODO: create a first comparison element variable
    first_celebrity = second_celebrity

    # TODO: create a second comparison element variable (diifferent from the first one)
    second_celebrity = random.choice(data)
    if first_celebrity == second_celebrity:
        second_celebrity = random.choice(data)

    # TODO: print first celebrity
    print(f"Compare A: {format_data(first_celebrity)}")

    # TODO: print vs
    print(vs)

    # TODO: print second celebrity
    print(f"Against B: {format_data(second_celebrity)}")

    # TODO: ask user for o a guess
    guess = input("Who has more followers? Type 'A' oor 'B': ")

    a_follower_count = first_celebrity["follower_count"]
    b_follower_count = second_celebrity["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")