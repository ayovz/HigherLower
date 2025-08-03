import random
import os
import time

from data import people, ascii_art


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_random_account(exclude=None):
    while True:
        account = random.choice(people)
        if account != exclude:
            return account


def compare_followers(a1, a2):
    if a1['followers'] >= a2['followers']:
        return 'A'
    else:
        return 'B'


def get_account_by_label(label, a1, a2):
    return a1 if label == 'A' else a2


def play_game():
    score = 0
    game_over = False

    while not game_over:
        account1 = get_random_account()
        account2 = get_random_account(account1)

        print("\nWho has more Instagram followers?")
        print(f"A: {account1['name']}, a {account1['description']} from {account1['country']}.")
        print(f"B: {account2['name']}, a {account2['description']} from {account2['country']}.")
        usr_ans = input("Your answer (A/B): ").strip().upper()

        if usr_ans not in ['A', 'B']:
            print("Invalid input. Please type A or B.")
            continue

        correct_ans = compare_followers(account1, account2)
        correct_account = get_account_by_label(correct_ans, account1, account2)

        if usr_ans == correct_ans:
            score += 1
            print(f"\n✅ Correct! {correct_account['name']} has {correct_account['followers']:,} followers.")
            print(f"🏆 Score: {score}")
        else:
            print(f"\n❌ Incorrect! {correct_account['name']} has {correct_account['followers']:,} followers.")
            print(f"Final Score: {score}")
            game_over = True


def main():
    replay = True
    while replay:
        clear_screen()
        print(ascii_art)
        play_game()

        again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            time.sleep(2)
            replay = False

        clear_screen()


if __name__ == "__main__":
    main()
