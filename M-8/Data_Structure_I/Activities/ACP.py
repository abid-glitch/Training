import random

low = 1
high = 5
tries = 12
hidden = random.randint(low, high)

def ask_guess():
    while True:
        val = int(input(f"Pick a number between {low} and {high}: "))
        if low <= val <= high:
            return val
        else:
            print("Try a valid number in range.")

def evaluate(guess, secret):
    if guess == secret:
        return "Correct"
    elif guess < secret:
        return "Too low"
    return "Too high"

def begin_game():
    attempts = 0
    success = False

    while attempts < tries:
        attempts += 1
        user_guess = ask_guess()
        outcome = evaluate(user_guess, hidden)
        if outcome == "Correct":
            print(f"You nailed it! Number was {hidden}. Attempts: {attempts}.")
            success = True
            break
        else:
            print(outcome, "Try again!")
    if not success:
        print(f"No luck! It was {hidden}.")

if __name__ == "__main__":
    print("Let's play the Guessing Game!")
    begin_game()
