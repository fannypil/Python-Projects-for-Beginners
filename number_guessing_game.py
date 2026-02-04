
import random

def main():
    attempts = 0
    try:
        min= int(input("Enter the minimum number (default 1):").strip())
        max= int(input("Enter the maximum number (default 100):").strip())
        if min >= max:
            print("Minimum value must be less than maximum value.")
            return
        num = random.randint(min, max)
        while True:
            try:
                guess= int(input(f"Guess the number between {min} and {max}:").strip())
                attempts += 1
                if attempts < 10:
                    if guess > num:
                        print(f"Too high! Try again. Attempts left: {10 - attempts}")
                    elif guess < num :
                        print(f"Too low! Try again. Attempts left: {10 - attempts}")
                    else:
                        print("Congratulations ! you guessed the number!")
                        break
                else:
                    print(f"Sorry, you've used all attempts. The number was {num}.")
                    break
            
            except ValueError:
                print("Please enter a valid number")
    except ValueError:
        print("Please enter valid integers for minimum and maximum values.")
    
      

if __name__ == "__main__":
    main()