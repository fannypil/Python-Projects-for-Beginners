import random


def main():
    # read only tuple
    options = ("r", "p", "s")
    emojies = {"r": "🪨", "p": "📃", "s": "✂️"}
    overall_player_statistics = {"win": 0, "lose": 0, "tie": 0}
    while True:
        computer_wins = 0
        user_wins = 0
        while computer_wins < 2 and user_wins < 2:
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
                overall_player_statistics["tie"] += 1
            elif (
                (user_choice == "r" and computer_choice == "s")
                or (user_choice == "p" and computer_choice == "r")
                or (user_choice == "s" and computer_choice == "p")
            ):
                print("You win!")
                user_wins += 1
                overall_player_statistics["win"] += 1
            else:
                print("You lose!")
                computer_wins += 1
                overall_player_statistics["lose"] += 1
        # Announce overall winner
        if user_wins == 2:
            print(f"You won the game! Score: {user_wins} to {computer_wins}")
        else:
            print(f"Computer won the game! Score: {computer_wins} to {user_wins}")

        # Ask if the user wants to Continue playing
        should_continue = input("Continue? (y/n): ").strip().lower()
        if should_continue == "n":
            print("Thanks for playing!")
            print("\n--- Session Statistics ---")
            print(f"Wins: {overall_player_statistics['win']}")
            print(f"Losses: {overall_player_statistics['lose']}")
            print(f"Ties: {overall_player_statistics['tie']}")
            break


if __name__ == "__main__":
    main()
