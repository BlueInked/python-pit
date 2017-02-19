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

