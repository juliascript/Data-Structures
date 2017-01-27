import permutation

def combination(data, k):
	permutedData = permutation(data)
	selection = []
	for i in range(k):
		selection.append(i)
	return selection