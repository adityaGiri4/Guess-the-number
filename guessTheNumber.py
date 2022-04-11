# Guess the number 

# Importing random module 
import random

# Making a function for user guess 
def user_guess(a):
    print(f"Computer have guessed a number between 0 and {a}")
    print("Now you have to guess that number")
    randomNumber = random.randint(0, a)
    guessNum = 0
    while guessNum != randomNumber:
        guessNum = int(input(f"Enter a number between 0 and {a}: \n"))
        if guessNum < randomNumber:
            print("Sorry, try again, you've entered a number too low")
        elif guessNum > randomNumber:
            print("Sorry, try again, you've entered a number too high")
        
    
    print(f"Yay, you've entered the exact number, computer guessed, which was {randomNumber}")
    print("Congrats")


# Making a function of  computer guess 
def computer_guess(y):
    low = 0
    high = y
    user_input = None
    print("Take a number between 0 and 15, keep it secret in your mind...")
    print("Let's see whether computer can guess it or not")
    ask = input("Start?, type 'yes' or 'no':\n")
    if ask == "yes":
        while user_input != "correct" :
            computerGuessed = random.randint(low, high)
            print("Computer guessed", computerGuessed)
            user_input = input(f"Type 'low' if {computerGuessed} is a low number than you thought, type 'high' if {computerGuessed} is a higher that what you thought, or type 'correct' if the computer the guessed the right number:\n ")
            if user_input == "low":
                computerGuessed += 1
            elif user_input == "high":
                computerGuessed -= 1
            elif user_input != "low" and user_input != "high" and user_input != "correct":
                print("Type 'low', 'high' and 'correct' for suitable outputs, try again...")
                    
        print("Wow, computer choosed the exact number which you thought, which was",computerGuessed)
    elif ask == "no":
        print("Ok, we will try later..")
    else:
        print("Something went wrong, try again....")



# Code execution by main function 
if __name__ == "__main__":
    askInput = int(input("Press 1 if you want to guess, or press 2 if you want computer to guess:\n"))
    if askInput == 1:
        user_guess(15)
    elif askInput == 2:
        computer_guess(15)
    else:
        print("Something went wrong, try again....")



