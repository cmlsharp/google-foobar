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


def convert2base(x, base):
    from string import digits, ascii_lowercase
    alnum = digits + ascii_lowercase
    if x < 0:
        sign = -1
    elif x == 0:
        return alnum[0]
    else:
        sign = 1
    x *= sign
    digits = list()
    while x:
        digits.append(alnum[x % base])
        x = int(x / base)
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)


def answer(n):
    currentbase = 2
    while True:
        conversion = str(convert2base(n, currentbase))
        if conversion == conversion[::-1]:
            return currentbase
        currentbase += 1
