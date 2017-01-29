#!python

import string


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # O(n/2)
    if text == '':
        return True
    lastIndex = len(text) - 1
    halfOfString = len(text) // 2
    for i in range(0, halfOfString):
        if text[i] == text[lastIndex]:
            # potential palindrome
            lastIndex -= 1
            continue
        else: 
            return False
    return True



def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    print left, right
    if text == '':
        return True

    if left is None or right is None: 
        left = 0
        right = len(text) - 1

    if right <= left:
        if text[left] == text[right]:
            return True
        else: 
            return False
    elif text[left] == text[right]:
        return is_palindrome_recursive(text, left + 1, right - 1)
    else: 
        return False


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
