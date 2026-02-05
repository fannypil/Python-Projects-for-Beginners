import random


def main():
    # read only tuple
    options = ("r", "p", "s")
    emojies = {"r": "🪨", "p": "📃", "s": "✂️"}
    while True:
        user_choice = input("Rock , Paper , Scissors ? (r/p/s)").strip().lower()
        if user_choice not in options:
            print("Invalid choice!")
            continue

        computer_choice = random.choice(options)

        print(f"You chose: {emojies[user_choice]}")
        print(f"Computer chose: {emojies[computer_choice]}")

        # determine winner
        if user_choice == computer_choice:
            print("Tie!")
        elif (
            (user_choice == "r" and computer_choice == "s")
            or (user_choice == "p" and computer_choice == "r")
            or (user_choice == "s" and computer_choice == "p")
        ):
            print("You win!")
        else:
            print("You lose!")

        # Ask if the user wants to Continue playing
        should_continue = input("Continue? (y/n): ").strip().lower()
        if should_continue == "n":
            break


if __name__ == "__main__":
    main()
