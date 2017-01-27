import permutation

def combination(data, k):
	permutatedData = permutation(data)
	selection = []
	for i in range(k):
		selection.append(i)
	return selection