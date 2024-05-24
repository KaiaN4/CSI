import random
import sys

values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
comparisons = ["2", "3", "4", "5", "6", "7", "8", "9", "1", "J", "Q", "K", "A"]
suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
card_deck = []


scorec = 0
scoreu = 0
cards_in_hand = 20

for value in values:
    for suit in suits:
        card_deck.append(f"{value} of {suit}")


    
while True:
    player = input("Do you want to play a card game?")
    
    if player == "no":
        sys.exit()
    elif player == "yes":
        played_deck = 
        while True:
            player1_hand = random.sample(card_deck, cards_in_hand)
            player2_hand = random.sample(card_deck, cards_in_hand)

        for i in range(0, cards_in_hand):
            input("Press enter to slam your card down")
            card1 = player1_hand[i]
            card2 = player2_hand[i]
            print(card1)
            print(card2)
            
            if comparisons.index(card1[0]) == comparisons.index(card2[0]):
                print("tie")
                print (f"p1: {scoreu} - p2: {scorec}")
            elif comparisons.index(card1[0]) > comparisons.index(card2[0]):
                print("player 1 wins")
                scoreu+=1
                print (f"p1: {scoreu} - p2: {scorec}")
            else:
                print("player 2 wins")
                scorec+=1
                print (f"p1: {scoreu} - p2: {scorec}")
