class Card():

    def __init__(self, rank, suit, point_value):
         self.rank = rank
         self.suit = suit
         self.point_value = point_value
         
    def __str__(self):
        return '{} of {} (Value = {})'.format(
            self.rank, self.suit, self.point_value)

    def change_ace(self):
        if self.rank == 'ACE':
            self.point_value = 1

    def is_equal(self, other):
        if self.rank == other.rank and self.suit == other.suit:
            return True
        return False

    def compare_cards(self, other):
        if self.is_equal(other):
            return 0
        elif self.rank == 'ACE' and other.rank != 'ACE':
            return 1
        elif self.rank != 'ACE' and other.rank == 'ACE':
            return -1
        elif self.point_value > other.point_value:
            return 1
        elif self.point_value < other.point_value:
            return -1
        else:
            ranks = ['TEN','JACK', 'QUEEN', 'KING', 'ACE']
            rank1 = ranks.index(self.rank)
            rank2 = ranks.index(other.rank)
            if rank1 > rank2:
                return 1
            elif rank1 < rank2:
                return -1
            else:
                suits = ['HEARTS', 'DIAMONDS', 'CLUBS', 'SPADES']
                suit1 = suits.index(self.suit)
                suit2 = suits.index(other.suit)
                if suit1 > suit2:
                    return 1
                else:
                    return -1
            
