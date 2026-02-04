
import random

def main():
    num = random.randint(1,100)
    while True:
       try:
        guess= int(input("Guess the number between 1 and 100:").strip())
        if guess > num:
            print("Too high! Try again.")
        elif guess < num :
            print("Too low! Try again.")
        else:
            print("Congratulations ! you guessed the number!")
            break
       
       except ValueError:
           print("Please enter a valid number")
      

if __name__ == "__main__":
    main()