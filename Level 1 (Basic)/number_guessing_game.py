import random


lowest_num = 1
highest_num = 100
max_guesses = 5
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"select a number between {lowest_num} and {highest_num}")
print(f"You have {max_guesses} guesses to find the number.")

while is_running:

    guess = input("Enter your guess:")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(
                f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False

        if is_running and guesses >= max_guesses:
            print(
                f"\nYou've reached the maximum number of guesses ({max_guesses}).")
            print(f"The answer was {answer}.")
            is_running = False

    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")


# def number_guessing_game():
#     print("=====================================")
#     print("Welcome to the Number Guessing Game! ")
#     print("I am thnking of a number between 1 and 100. ")
#     secret_number = random.randint(1, 100)

#     attempts = 0
#     while True:
#         try:
#             user_guess = int(input("\nEnter your guess: "))
#             attempts += 1
#             if user_guess < 1 or user_guess > 100:
#                 print("Please enter a number between 1 and 100.")
#             elif user_guess < secret_number:
#                 print("Too low! Try a higher number.")
#             elif user_guess > secret_number:
#                 print("Too high! Try a lower number.")
#             else:
#                 print(f"\n CONGRATULATIONS! You guessed it right!")
#                 print(f" It took you {attempts} attempts to find the number {secret_number}.")
#         except ValueError:
#             print("Invalid input! Please enter a valid integer number.")

#             if __name__ == "__main__":
#                 number_guessing_game()
