import random


def main():
    best_score = float("inf")
    while True:
        attempts = 0
        try:
            min = int(input("Enter the minimum number (default 1):").strip())
            max = int(input("Enter the maximum number (default 100):").strip())
            if min >= max:
                print("Minimum value must be less than maximum value.")
                return
            num = random.randint(min, max)
            while True:
                try:
                    guess = int(
                        input(f"Guess the number between {min} and {max}:").strip()
                    )
                    attempts += 1
                    if attempts < 10:
                        if guess > num:
                            print(
                                f"Too high! Try again. Attempts left: {10 - attempts}"
                            )
                        elif guess < num:
                            print(f"Too low! Try again. Attempts left: {10 - attempts}")
                        else:
                            print("Congratulations ! you guessed the number!")
                            if attempts < best_score:
                                best_score = attempts
                                print(f"New best score: {best_score} attempts!")
                            else:
                                print(
                                    f"You took {attempts} attempts. Best score: {best_score} attempts."
                                )
                            break
                    else:
                        print(f"Sorry, you've used all attempts. The number was {num}.")
                        print(f"Best score so far:{best_score} attempts")
                        break

                except ValueError:
                    print("Please enter a valid number")
            play_again = input("Do you want to play again? (y/n):").strip().lower()
            if play_again != "y":
                print("Thanks for playing!")
                break
        except ValueError:
            print("Please enter valid integers for minimum and maximum values.")


if __name__ == "__main__":
    main()
