import random
from recursion import factorial

def permutation(data):
	# this is very shitty performance
	#  theoretically can go on forever, lol
	numberOfPossibilities = factorial(len(data))
	possibilitiesList = []
	while len(possibilitiesList) > numberOfPossibilities:
		randomShuffle = random.shuffle(data)
		if randomShuffle in possibilitiesList:
			continue
		else: 
			possibilitiesList.append(randomShuffle)
	return possibilitiesList