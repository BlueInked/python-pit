'''Create a program that will play the “cows and bulls” game with the user.
The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have
a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.”
Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
Once the user guesses the correct number, the game is over. Keep track of the number
of guesses the user makes throughout teh game and tell the user at the end.
'''
import random

def num_guess(ran_num, guessed_num):
    '''
    num  -> list

    Returns the number of cows and bulls from he guesses a person makes to find a random number

    '''
    
    #Function to keep count of the cows and bulls
    cows_bulls = [0,0]
    
    for i in range(len(ran_num)):
        if ran_num[i] == guessed_num[i]:
            cows_bulls[1]+=1
        else:
            cows_bulls[0]+=1
    return cows_bulls

if __name__=="__main__":
    playing = True 
    ran_num = str(random.randint(0,9999)) #random 4 digit number
    guesses = 0

    print("Let's play a game of Cowbull!") #the rules
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")

    while playing:
        guessed_num = input("Give me your best guess!")
        if guessed_num == "exit":
            break
        cows_bulls_count = num_guess(ran_num,guessed_num)
        guesses+=1

        print("You have "+ str(cows_bulls_count[0]) + " cows, and " + str(cows_bulls_count[1]) + " bulls.")

        if cows_bulls_count[1]==4:
            playing = False
            print("You win the game after " + str(guesses) + "! The number was "+str(ran_num))
            break #redundant exit
        else:
            print("Your guess isn't quite right, try again.")
