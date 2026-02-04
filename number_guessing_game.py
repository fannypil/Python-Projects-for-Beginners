
import random

def main():
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
                if guess > num:
                    print("Too high! Try again.")
                elif guess < num :
                    print("Too low! Try again.")
                else:
                    print("Congratulations ! you guessed the number!")
                    break
            
            except ValueError:
                print("Please enter a valid number")
    except ValueError:
        print("Please enter valid integers for minimum and maximum values.")
    
      

if __name__ == "__main__":
    main()