import random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        for s in SUITS:
            if s == suit:
                self.suit = suit
                self.suit_index = SUITS.index(suit)
                break
        for r in RANKS:
            if r == rank:
                self.rank = rank
                self.rank_index = RANKS.index(rank)
                break
    def __eq__(self, other):
        if (self.rank_index == other.rank_index) & (self.suit_index == other.suit_index):
            return True
        return False

    def __lt__(self, other):
        same_rank = False
        if self.rank_index == other.rank_index:
                same_rank = True
        if self.rank_index < other.rank_index:
            return True
        if (self.suit_index < other.suit_index) & same_rank:
            return True
        return False

    def __gt__(self, other):
        same_rank = False
        if self.rank_index == other.rank_index:
            same_rank = True
        if self.rank_index > other.rank_index:
            return True
        if (self.suit_index > other.suit_index) & same_rank:
            return True
        return False
    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"
