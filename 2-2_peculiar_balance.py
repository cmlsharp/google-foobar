"""
Peculiar balance
================
Can we save them? Beta Rabbit is trying to break into a lab that contains the only known zombie cure - but there's an
obstacle. The  door will only open if a challenge is solved correctly. The future of the zombified rabbit population is
at stake, so Beta reads the  challenge: There is a scale with an object on the left-hand side, whose mass is given in
some number of units. Predictably, the task is to  balance the two sides. But there is a catch: You only have this
peculiar weight set, having masses 1, 3, 9, 27, ... units. That is, one  for each power of 3. Being a brilliant
mathematician, Beta Rabbit quickly discovers that any number of units of mass can be balanced  exactly using this set.
To help Beta get into the room, write a method called answer(x), which outputs a list of strings representing where the
weights should be  placed, in order for the two sides to be balanced, assuming that weight on the left has mass x units.
The first element of the output list should correspond to the 1-unit weight, the second element to the 3-unit weight,
and so on. Each  string is one of:
"L" : put weight on left-hand side
"R" : put weight on right-hand side
"-" : do not use weight
To ensure that the output is the smallest possible, the last element of the list must not be "-".
x will always be a positive integer, no larger than 1000000000.
"""
# This function is basically the same as the one found in 1-1_pallindrome.py except 
# it is specifically for converting to ternary (base 3)
def nearestpowerof3(x):
    numbers = '012'
    if x < 0:
        sign = -1
    elif x == 0:
        return numbers[0]
    else:
        sign = 1
    x *= sign
    digits = list()
    while x:
        digits.append(numbers[x % 3])
        x = int(x / 3)
    if sign < 0:
        digits.append('-')
    digits.reverse()
    # Here's where it differs. The concept here is that the number of digits a number is when
    # converted into ternary, corresponds with the exponent of the next power of three greater than that number
    # e.g. 26 is '222', thus the next greatest power of 3 is 3**3 aka 27.
    exp = int(len(''.join(digits)))
    return exp


def answer(x):
    product = []
    # Add the object's weight to the left side
    left = [x]
    right = []
    """
    The following algorithm starts with the next greatest power of 3 and works it's way down
    It calculates the difference between the two sides and, if adding the weight to the right side will
    decrease the absolute value of the difference, it adds it. Same with the left. If adding it to either
    side would not decrease the difference at all, it discards it.
    """
    for power in range(nearestpowerof3(x), -1, -1):
        diff = sum(left) - sum(right)
        if abs(sum(left) + 3**power - sum(right)) < abs(diff):
            left.append(3**power)
            product.append('L')
        elif abs(sum(left) - (3**power + sum(right))) < abs(diff):
            right.append(3**power)
            product.append('R')
        else:
            product.append('-')
    # If the solution begins (yes, begins. This list still needs to be reversed. See below) with a '-', remove it.
    if product[0] == '-':
        product = product[1:]
    # Of course the above algorithm creats the list starting from the largest power. The question asks 
    # for the list to start with the 1 unit weight first. Thus, we hve to revert the list.
    return list(reversed(product))
