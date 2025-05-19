import random  # Step 1: Import random module for secret number generation

# Step 2: Generate a secret number between 1 and 10
secret_number = random.randint(1, 10)

# Step 3: Define game variables
guesses_left = 5
user_guess = 0 

# Step 4: Game loop
while guesses_left > 0:
    try:
        # Step 5: Prompt user for input
        user_guess = int(input(f"\nGuess a number between 1 and 10 (Attempts left: {guesses_left}): "))

        # Step 6: Check and respond
        if user_guess == secret_number:
            print("🎉 Congratulations! You guessed the number!")
            break
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")

        guesses_left -= 1  

    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 10.")

# Step 7: Check if game ended without a win
if guesses_left == 0 and user_guess != secret_number:
    print(f"\n💥 Out of guesses! The correct number was {secret_number}. Better luck next time!")
