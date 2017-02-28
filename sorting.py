def swap(arr, i1, i2):
	arr[i1], arr[i2] = arr[i2], arr[i1]

def bubble_sort(arr):
	_sorted = False

	while not _sorted:
		_sorted = True
		for i in range(len(arr) - 1):
			if arr[i] > arr[i + 1]:
				swap(arr, i, i + 1)
				_sorted = False
	return arr
		

def insertion_sort(arr, sorted_list=None):
	element = arr[0]

	if sorted_list is None:
		sorted_list = []
		sorted_list.append(element)

	# binary search sorted list to find spot 
	index = binary_search(arr, element)
	sorted_list.insert(index)
	insertion_sort(arr[1:], sorted_list)


def binary_search(arr, element, left=0):
	middle_index = len(arr)  // 2
	if element == arr[middle_index]:
		return middle_index + left
	if element < arr[middle_index]:
		return binary_search(arr[:middle_index], element)
	elif element > arr[middle_index]:
		return binary_search(arr[middle_index + 1:], element, middle_index + 1)


def selection_sort(arr, sorted_list=None):
	if sorted_list is None:
		sorted_list = []
	# find smallest num
	smallest = arr[0]

	for i in range(len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]

	sorted_list.append(smallest)
	del(smallest)
	if len(arr) == 0:
		return sorted_list
	else: 
		return selection_sort(sorted_list)

def combine(arr1, arr2):
	sa = []
	i1 = 0
	i2 = 0
	p1 = arr1[i1]
	p2 = arr2[i2]
	while p1 is not None or p2 is not None:
		try:
			if p1 < p2: 
				sa.append(p1)
				p1 = arr1[i1 + 1]
			else: 
				sa.append(p2)
				p2 = arr2[i2 + 1]
		except IndexError:
			break

	if i1 < len(arr1) - 1:
		sa.append(arr1[i1:])
	elif i2 < len(arr2) - 1:
		sa.append(arr2[i2:])

	return sa

def merge_sort(arr):
    if len(arr) > 1:
        middle_index = len(arr) // 2
        first_half = arr[:middle_index]
       	second_half = arr[middle_index:]
        sorted_list = combine(bubble_sort(first_half), bubble_sort(second_half))
	return sorted_list


def counting_sort(arr):
	pass

def bucket_sort(arr):
	pass


if __name__ == '__main__':
	a = [0, 13, 6, 3, 18]
	print merge_sort(a)
