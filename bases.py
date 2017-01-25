#!python

import string, math


def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    assert 2 <= base <= 36
    # TODO: Decode number

    if base == 10:
        return int(str_num)
    
    if base < 10:
        digits = list(str_num)
        numInBaseTen = 0
        numOfDigits = digits.__len__()
        power = 0
        for i in range(numOfDigits, 0, -1):
            digitRepresentation = int(math.pow(base, power))
            numInBaseTen += int(digits[i - 1]) * digitRepresentation
            power += 1
        return numInBaseTen
    # else:





def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    assert 2 <= base <= 36
    # TODO: Encode number
    letters = list(string.ascii_lowercase)
    mods = []
    while (num >= base):
        mod = num % base
        mod = int(mod)
        if mod > 9:
            mods.insert(0, letters[mod-10])
        else:
            mods.insert(0, "%d" % mod)
        num = int(math.floor(num / base))
    
    num = int(num)
    mods.insert(0, "%d" % num)
    return string.join(mods, '')


def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """
    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36
    # TODO: Convert number


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
