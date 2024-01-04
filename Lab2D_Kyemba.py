from CARDS import *
from ModifiedWarHand import *
import random as rand

# main code
letsPlay = input('Would you like to play a game? Y/N: ')

while letsPlay == 'Y':

    # creating the decks for player 1 and player 2
    ranks = ['ACE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN',
             'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING']
    points = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    suits = ['SPADES', 'HEARTS', 'DIAMONDS', 'CLUBS']
    deck = [] 
    for i in range(13):
        for suit in suits:
            deck.append(Card(ranks[i], suit, points[i]))
    rand.shuffle(deck)

    player1cards = []
    player2cards = []

    while len(deck) > 0:
        player1cards.append(deck[0])
        deck.pop(0)
        player2cards.append(deck[0])
        deck.pop(0)
        
    p1deck = ModifiedWarDeck(player1cards)
    p2deck = ModifiedWarDeck(player2cards)

    # main game play
    count = 0
    while p1deck.endit() == True and p2deck.endit() == True:
        i = 0
        player1turn = []
        player2turn = []
        
        player1turn.append(p1deck.play())
        player2turn.append(p2deck.play())

        if (player1turn[i].point_value == player2turn[i].point_value):
            while (p1deck.endit() == True and p2deck.endit() == True):           
                player1turn.append(p1deck.play())
                player2turn.append(p2deck.play())
                i += 1
                if (player1turn[i].point_value > player2turn[i].point_value):
                    p1deck.add_to_discard_pile(player1turn)
                    p1deck.add_to_discard_pile(player2turn)
                    break
                elif (player1turn[i].point_value < player2turn[i].point_value):
                    p2deck.add_to_discard_pile(player1turn)
                    p2deck.add_to_discard_pile(player2turn)
                    break
                count += 1
            
        elif (player1turn[i].point_value > player2turn[i].point_value):
            p1deck.add_to_discard_pile(player1turn)
            p1deck.add_to_discard_pile(player2turn)
            
        else:
            p2deck.add_to_discard_pile(player1turn)
            p2deck.add_to_discard_pile(player2turn)
        
        count += 1
    
    if len(p1deck) > len(p2deck):
        print('P1- Wins\n\n{}'.format(count))
    else:
        print('P2- Wins\n\n{}'.format(count))

    letsPlay = input('Would you like to play again? Y/N: ')
