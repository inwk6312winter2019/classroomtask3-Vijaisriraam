"""
rank=[1,2,3,4,5,6,7,8,9,10,11,12,13]
suite=['H','S','D','C']

cards=list(zip(rank,suite))
cards=[]
for ranks in rank:
	cards+=[(ranks,suite[0]),(ranks,suite[1]),(ranks,suite[2]),(ranks,suite[3])]

print(cards)
"""

class card():

	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']

	def __init__(self,rank=0,suite=2):
		self.rank=rank
		self.suite=suite

	def __str__(self):
		return f"The rank is {card.rank_names[self.rank]} and the suit is {card.suit_names[self.suite]}"
		

ace_of_spade=card(2,3)
print(ace_of_spade)
