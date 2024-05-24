import random#enters the random library for use of random functions
import sys#enters the system library for the exit() function

game = ['rock', 'paper', 'scissors']#creates a list with possible answers for playing the game

scoret = 0#creates a variable for the score for player 1 and starts at 0
scoreu = 0#creates a variable for the score for player 2/computer and starts at 0
while True:
    while True:#an infinite loop(while condition True is true)
        bot_or_player = str.lower(input("Play against bot or player: "))#asks the user if they want to play against another player or a bot

        if bot_or_player == "stop":#if the user enters 'stop'
            sys.exit()#manually breaks the code
        elif bot_or_player == "player":#if player 1 chooses to play with another player
            p2 = str.lower(input('Rock, paper, scissors'))#has player 2/computer randomly choose from the list game
            print ("\n" *49)#enters 49 new lines
            break#manually breaks the loop

        elif bot_or_player == "bot":#if player 1 chooses to play with a bot
            p2 = random.choice(game)#has the player 2/computer randomly choose from the list game
            break#manually breaks the loop
            
        else:#if player 1 prints anything other than bot, player, or stop
            print ('invalid answer')#print 'invalid answer'
            

    while True:#an infinite loop(while condition True is true)
        p1 = str.lower(input('Rock, paper, scissors'))#prompts the user to choose either rock, paper, or scissors

        if p1 == 'stop':#if the user enters 'stop'
            sys.exit()#manually breaks the code
            
        elif (p1 == p2):#if  player 1 and player 2/computer both print the same answer
            print('It is a Tie!')#print 'It is a Tie!'
            print (f"p1: {scoret} - p2: {scoreu}")#enters the score of player 1 and the score of player 2/computer
            break
        elif (p1 == 'rock'):#if the user enters 'rock'
            if (p2 == 'paper'):#if the player 2/computer chooses 'paper'
                print('Player 2 Wins!')#print 'Player 2 Wins!'
                scoreu+=1#adds one score to player 2/computer
                print (f"p1: {scoret} - p2: {scoreu}")#enters the score of player 1 and the score of player 2/computer
                break#manually breaks the loop
            elif (p2 == 'scissors'):#if player 2/computer chooses 'scissors'
                print('Player 1 Wins!')#print 'You Win!'
                scoret+=1#adds one score to player 1
                print (f"p1: {scoret} - p2: {scoreu}")#enters the score of player 1 and the score of player 2/computer
                break#manually breaks the loop
        elif(p1 == 'paper'):#if player 1 enters 'paper'
            if (p2 == 'rock'):#if player 2 /computer chooses 'rock'
                print ('Player 1 Wins!')#print 'You Win!'
                scoret+=1#adds one score to player 1
                print (f"p1: {scoret} - p2: {scoreu}")#enters the score of player 1 and the score of player 2/computer
                break#manually breaks the loop
            elif (p2 == 'scissors'):#if player 2/computer chooses 'scissors'
                print ('Player 2 Wins!')#print 'Player 2 Wins!'
                scoreu+=1#adds one score to player 2/computer
                print (f"p1: {scoret} - p2: {scoreu}")#enters the score of the user and the score of the computer
                break#manually breaks the loop
        elif(p1 == 'scissors'):#if the user enters 'scissors'
            if(p2 == 'rock'):#if the computer chooses 'rock'
                print('Player 2 Wins!')#print 'Player 2 Wins!'
                scoreu+=1#adds one score to the computer
                print (f"p1: {scoret} - p2: {scoreu}")#enters the score of player 1 and the score of player 2/computer
                break#manually breaks the loop
            elif(p2 == 'paper'):#if player 2/computer chooses 'paper'
                print('Player 1 Wins!')#print 'You Win!'
                scoret+=1#adds one score to player 1
                print (f"p1: {scoret} - p2: {scoreu}")#enters the score of player 1 and the score of player 2/computer
                break#manually breaks the loop
        else:#if player 1 or player 2 print anything other than 'rock', 'paper', or 'scissors'
            print ('invalid answer')#print invalid answer

        if scoret >= 10 or scoreu >= 10:#if either one of the scores is greater than or equal to 10
            print ('Wow that is a lot of rounds')#enters 'Wow that is a lot of rounds'
            break#manually breaks the loop

    while True:#an infinite loop(while condition True is true)
        p1 = str.lower(input('Do you want to play again?'))#prompts player 1 if they want to play again

        if p1 == 'no':#if player 1 says no
            print ('Hope you had fun!')#enters 'Hope you had fun!'
            sys.exit()#manually breaks the code
        elif p1 == 'yes':#if player 1 says yes
            break
            if bot_or_player == "player":#if there was another player and player 1 entered yes
                p2 = str.lower(input('Do you want to play again?'))#asks player 2 if they want to play again
                if p2 == 'no':#if player 2 says no
                    print ('Hope you had fun!')#enters 'Hope you had fun!'
                    sys.exit()#manually breaks the code
