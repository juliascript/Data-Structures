#!python

import string, math


def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    assert 2 <= base <= 36

    # if method is called with a num already in base 10, just return it as an int
    if base == 10:
        return int(str_num)
    
    # create a list of characters that might be letters or digits from argument string 
    # wtf do I call it?? 
    digits = list(str_num)

    numInBaseTen = 0
    # store the amount of "digits" that have to be iterated over
    numOfDigits = digits.__len__()
    # var for the power to raise the base to, I'm iterating backwards so I need this var
    power = 0

    # store letters a-z in list
    letters = list(string.ascii_lowercase)
    # iterating backwards, for as many times as there are "digits" in the arg number
    for i in range(numOfDigits, 0, -1):
        # calculating the value that the placing of the digit represents, using a power var
        #   that is increased by one each iteration
        placeValue = int(math.pow(base, power))
        # if the "digit" turns out to be a letter (thanks, bases 11+)
        # -- note: [i - 1] accounts for iterating from len of array to 1
        if digits[i - 1] in letters:
            # find the letter's corresponding index in the letters array and add 10 
            #   to account for digits 0-9 before it
            numInDigitSlot = int(letters.index(digits[i - 1]) + 10)
        else: 
            # if it's an actual digit, just convert it into an int
            numInDigitSlot = int(digits[i - 1])
        # calculating the value represented by multiplying the digit and place value
        #   and adding that to the total in base 10
        numInBaseTen += numInDigitSlot * placeValue
        # increase power var by one so next placeValue calculation will be accurate
        power += 1

    return numInBaseTen


def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    assert 2 <= base <= 36

    # if method is called with a num already in base 10, just return it as an int
    if base == 10:
        return str(num)

    # store letters a-z in list
    letters = list(string.ascii_lowercase)
    # if the number is larger than the base we're converting to, meaning it will 
    # take more than one place value in the target base to represent this number
    if num > base:
        # for storing the remainders of each division
        mods = []
        # if the number is still divisible by the base, either equally or with remainders
        # -- note: dividing by the base because each place value represents a power raised to it
        while (num >= base):
            # get the remainder of the division
            mod = num % base
            # convert it to an int
            mod = int(mod)
            if mod > 9:
                # use a letter representation of the remainder bc it's larger than 9
                # -- note: prepending because the power is increasing as num gets smaller
                #           .. place values increase by the power raised to the base each step
                mods.insert(0, letters[mod - 10])
            else:
                # remainder is between 0 and 9
                mods.insert(0, "%d" % mod)
            # num is redefined as the dividend, rounded down (accounting for this through mods)
            # -- note: while loop will continue to run until num is no longer divisible by the base
            num = int(math.floor(num / base))
        # convert to an int
        num = int(num)
        # 
        mods.insert(0, "%d" % num)
        # return 
        return string.join(mods, '')
    else: 
        # if the number is smaller than the base, meaning it can be represented in one place value

        # if the num is less than 10, it doesn't need to be represented with a letter
        if num < 10:
            # convert to a string and return
            return str(num)
        else: 
            # return the corresponding letter, accounting for the 10 
            #   digits before letters are necessary (0-9)
            return letters[num - 10]


def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """
    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36
    # decode from initial base into base10
    numInBaseTen = decode(str_num, base1)
    # encode base10 num into target base 
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
