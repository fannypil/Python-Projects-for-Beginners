import random

def roll_dice():
    return random.randint(1,6)

def main():
    while True:
        choice = input("Roll the dice? (y/n): ").strip().lower()
        if choice == 'y':
            n = input("How many dice to roll?").strip()
            if n.isdigit() and int(n)>0:
                n=int(n)
                results  = []
                for _ in range(n):
                    results.append(roll_dice())
                if n==1:
                    print(f"({results[0]})")
                else:
                    print(tuple(results))
            else:
                print("Please enter a valid positive integer.")
        elif choice == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
