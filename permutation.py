import random
from recursion import factorial

def permutation(data):
	# this is very shitty performance
	#  theoretically can go on forever, lol
	#  and probably will go on forever when n is bigger than like 10 
	
	# numberOfPossibilities = factorial(len(data))
	# possibilitiesList = []
	# while len(possibilitiesList) > numberOfPossibilities:
	# 	randomShuffle = random.shuffle(data)
	# 	if randomShuffle in possibilitiesList:
	# 		continue
	# 	else: 
	# 		possibilitiesList.append(randomShuffle)
	# return possibilitiesList