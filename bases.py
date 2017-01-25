#!python

import string, math


def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    assert 2 <= base <= 36

    if base == 10:
        return int(str_num)
    
    digits = list(str_num)
    numInBaseTen = 0
    numOfDigits = digits.__len__()
    power = 0

    letters = list(string.ascii_lowercase)
    for i in range(numOfDigits, 0, -1):
        digitRepresentation = int(math.pow(base, power))
        if digits[i - 1] in letters:
            numInDigitSlot = int(letters.index(digits[i - 1]) + 10)
        else: 
            numInDigitSlot = int(digits[i - 1])
        numInBaseTen += numInDigitSlot * digitRepresentation
        power += 1

    return numInBaseTen
        






def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    assert 2 <= base <= 36

    if base == 10:
        return str(num)

    letters = list(string.ascii_lowercase)
    if num > base:
        mods = []
        while (num >= base):
            mod = num % base
            mod = int(mod)
            if mod > 9:
                mods.insert(0, letters[mod - 10])
            else:
                mods.insert(0, "%d" % mod)
            num = int(math.floor(num / base))
        
        num = int(num)
        mods.insert(0, "%d" % num)
        return string.join(mods, '')
    else: 
        if num < 10:
            return str(num)
        else: 
            return letters[num - 10]


def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """
    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36
    numInBaseTen = decode(str_num, base1)
    numInSpecifiedBase = encode(numInBaseTen, base2)
    return numInSpecifiedBase


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        str_num = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        result = convert(str_num, base1, base2)
        print('{} in base {} is {} in base {}'.format(str_num, base1, result, base2))
    else:
        print('Usage: {} number base1 base2'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
