import random
from replit import clear
from art import logo, vs
from game_data import data


def get_random_account():
    '''Get data from random account in game_data file'''
    return random.choice(data)


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, {description}, from {country}"


def check(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    elif a_followers < b_followers:
        return guess == "b"


def game():
    '''The player tries to choose a person with a higher number of followers every time. The second choice keeps on becoming the first choice and the second choice is a random choice every time.'''
    print(logo)
    score = 0
    game_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Compare B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']
        is_correct = check(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right. Your current score is {score}.")
        else:
            game_continue = False
            print(f"Game over. Try again! Your final score: {score}")


game()