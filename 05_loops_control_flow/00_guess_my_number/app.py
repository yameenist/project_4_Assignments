import random

def main():
    # Generate the secret number at random!
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")
    
    # Get user's guess
    guess = int(input("Enter a guess: "))
    
    # Loop until the user guesses correctly
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
            
        print()  # Print an empty line for better readability
        guess = int(input("Enter a new guess: "))  # Get a new guess
        
    print("Congrats! The number was: " + str(secret_number))
    
if __name__ == '__main__':
    main()

