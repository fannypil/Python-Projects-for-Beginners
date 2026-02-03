import random

def roll_dice():
    return random.randint(1,6)

def main():
    while True:
        choice = input("Roll the dice? (y/n): ").strip().lower()
        if choice == 'y':
            result1 = roll_dice()
            result2 = roll_dice()
            print(f"({result1}, {result2})")
        elif choice == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
