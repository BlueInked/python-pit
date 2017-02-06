


def rps():
    ''' str -> str

    Returns a sring of who wins when given two players Rock Paper Scissor choices

    '''
    quit = input('Type "Q" to quit:' )
    while quit != "Q":
        player1 = input("Choose: rock paper or scissors:")
        player2 = input("Now you choose: rock paper scissors:")
        if player1 == "paper" and player2 == "rock" or player1 == "rock" and player2 == "scissors"  or player1 == "scissors" and player2 == "paper":
            print("Player1 Wins")
            quit = input('Type "Q" to quit:' )
        elif player2 == "paper" and player1 == "rock" or player2 == "rock" and player1 == "scissors"  or player2 == "scissors" and player1 == "paper":
            print("Player2 Wins")
            quit = input('Type "Q" to quit:' )
        elif player1 == player2:
            print("It's a Tie!")
            quit = input('Type "Q" to quit:' )
        elif player1 or player2 != "paper" or "scissors" or "rock":
            print("Please Try Again")
            quit = input('Type "Q" to quit:' )
            

   

    

       




