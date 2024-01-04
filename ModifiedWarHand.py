# ModifiedWarDeck Kyemba

from CARDS import *
import random as rand

class ModifiedWarDeck():

    def __init__(self, cards):
        self.hand_list = []
        self.hand_list.extend(cards)
        self.discard_pile = []
        
    def __str__(self):
        x = '\n'.join(map(str, self.hand_list))
        return x
    
    def __len__(self):
        return len(self.hand_list)

    def shuffle(self):
        rand.shuffle(self.hand_list)

    def play(self):
        if len(self.hand_list)>0:
            drawn = self.hand_list.pop(0)
            return drawn
        else:
            i = 0
            while i < len(self.discard_pile):
                self.hand_list.append(self.discard_pile[i])
                self.discard_pile.pop(i)
            self.shuffle()
            drawn = self.hand_list.pop(0)
            return drawn
   
    def add_to_discard_pile(self, cards):
        self.discard_pile.extend(cards)

    def display_discard(self):
        if len(self.hand_list) > 0:
            print('\n'.join(map(str, self.discard_pile)))
        else:
            print('DISCARD PILE EMPTY')

    def endit(self):
        if len(self.hand_list) > 0 or len(self.discard_pile) > 0:
            return True
        return False
