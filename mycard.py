"""
rank=[1,2,3,4,5,6,7,8,9,10,11,12,13]
suite=['H','S','D','C']

cards=list(zip(rank,suite))
cards=[]
for ranks in rank:
	cards+=[(ranks,suite[0]),(ranks,suite[1]),(ranks,suite[2]),(ranks,suite[3])]

print(cards)
"""

import random 

class card():

	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']


	def __init__(self,rank=0,suite=2):
		self.rank=rank
		self.suite=suite

	def __str__(self):
		return f"The rank is {card.rank_names[self.rank]} and the suit is {card.suit_names[self.suite]}"
		

	def __lt__(self, other):
                # check the suits
                if self.suit < other.suit: return True
                if self.suit > other.suit: return False
                # suits are the same... check ranks
                return self.rank < other.rank

	def __eq__(self,other):
		return self.rank==other.rank and self.suit==other.suit
	

class Deck:
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				self.card = card(suit, rank)
				self.cards.append(card)


	def pop_card(self):
		return self.cards.pop()

	def add_card(self, card):
		self.cards.append(card)

	def shuffle(self):
		random.shuffle(self.cards)


class Hand(Deck):
	def __init__(self, label=''):
		self.cards = []
		self.label = label


deck=Deck()
card=deck.pop_card()
Hand.add_card(card)
print(hand)
#mycards=Deck()

ace_of_spade=card(2,3)
print(ace_of_spade)
