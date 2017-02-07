import random


def number_guess():
    ''' int -> str

    Returns a string of whether a person has guessed the right random number
    
    '''
    number = random.randint(1,9)
    
    play2 = input("Wanna play again?:")
    exit = input('Type "E" to exit:')
    while quit != "E" or play2 != "no":
        guess = input("I'm thinking of a number between 1 and 9 try to guess it:")
        if int(guess) == number:
            print("You guessed correctly! ")
            play2 = input("Wanna play again?:")
            break
        elif int(guess) < number:
            print("Your guess is too low. Try Again.")
            guess
        elif int(guess) > number:
            print("Your guess is too high. Try Again." )
            guess
            '''
        elif int(guess) > 9:
            print("Either you did not choose a number between 1-10 or you did not pick a number.  Pick a number or Exit")
            exit = input('Type "E" to exit:')
        
            

   

    

       




