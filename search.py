#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # omega(1), O(n)
    if item == array[index]:
        return index
    else: 
        if index < len(array) - 1:
            return linear_search_recursive(array, item, index + 1)
        else: 
            return None
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests below


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # omega(1), O(logn)
    lowerBound = 0
    upperBound = len(array)

    while lowerBound < upperBound:
        midIndex = (lowerBound + ((upperBound - lowerBound) // 2))
        itemAtIndex = array[midIndex]
        if item == itemAtIndex: 
            return midIndex
        elif item > itemAtIndex:
            lowerBound += 1
        elif item < itemAtIndex:
            upperBound = midIndex

    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests below


def binary_search_recursive(array, item, left=None, right=None):
    # omega(1), O(logn)
    if left == None:
        left = 0 
        right = len(array) - 1

    midIndex = ((left + right) // 2)
    itemAtIndex = array[midIndex]

    if right - left < 0:
        return None
    else: 
        if item == itemAtIndex:
            return midIndex
        elif item > itemAtIndex:
            left = midIndex + 1
        elif item < itemAtIndex:
            right = midIndex - 1

        return binary_search_recursive(array, item, left, right)









