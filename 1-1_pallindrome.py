"""
Palindrome
==========

To help Beta Rabbit crack the lock, write a function answer(n) which returns the
smallest positive integer base b, at least 2, in which the integer n is a
palindrome. The input n will satisfy "0 <= n <= 1000".

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) n = 0
Output:
    (int) 2

Inputs:
    (int) n = 42
Output:
    (int) 4
"""
from __future__ import division # Not actually necessary but good for Python 3 compatibility

def convert2base(x, base):
    # string.digits and string.ascii_lowercase are strings that
    # contain digits and lowercase letters respectively.
    from string import digits, ascii_lowercase
    # alnum would equal 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c...
    alnum = digits + ascii_lowercase
    if x < 0:
        sign = -1
    elif x == 0:
        return alnum[0]  # 0 in any base is 0
    else:
        sign = 1
    x *= sign # Temporarily make negative numbers positive
    digits = list()
    while x: # Shorthand for while x > 0
        # Divide our number by the base, the 
        # remainder becomes part of our answer
        # while the quotient becomes our new number.
        digits.append(alnum[x % base])
        x = int(x // base)
    if sign < 0:
        digits.append('-') # Make negative numbers negative again
    # The above process returns our answer backwords. 
    # We need to reverse it
    digits.reverse() 
    return ''.join(digits)


def answer(n):
    currentbase = 2
    while True:
        conversion = str(convert2base(n, currentbase))
        # The third field in slicing specifies the 'step'
        # A step of negative one means read backwards
        if conversion == conversion[::-1]:
            return currentbase
        currentbase += 1
