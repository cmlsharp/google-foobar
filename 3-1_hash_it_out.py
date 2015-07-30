"""
Hash it out
===========

Something horrible must have gone wrong in that last mission. As you wake in a holding cell, you realize that you're in
the clutches of Professor Booleans numerous but relatively incompetent minions! Time to plan another escape. Lucky for
you nobody is around (do these security minions just sleep all the time?), so you have a chance to examine your cell.
Looking around, you see no signs of surveillance (ha, they must underestimate you already) and the only thing keeping
you contained is an electronic door lock. Should be easy enough.

You and Beta Rabbit worked together to exfiltrate some of Professor Booleans security information in anticipation of a
moment just like this one. Time to put it to the test.

If memory serves, this locking mechanism relies on a horribly bad cryptographic hash, and you should be able to break it
with some rudimentary calculations.

To open these doors, you will need to reverse engineer the hash function it is using. You already managed to steal the
details of the algorithm used, and with some quiet observation of the guards you find out the results of the hash (the
digest). Now to break it.

The function takes a 16 byte input and gives a 16 byte output. It uses multiplication (*), bit-wise exclusive OR (XOR)
and modulo (%) to calculate an element of the digest based on elements of the input message:

digest [i] = ( (129 * message[i]) XOR message[i-1]) % 256

For the first element, the value of message[-1] is 0.

For example, if message[0] - 1 and message[1] = 129, then:

For digest[0]: 129*message[0] = 129
129 XOR message[-1] = 129
129 % 256 = 129
Thus digest[0] = 129.

For digest[1]: 129*message[1] = 16641
16641 XOR message[0] = 16640
16640 % 256 = 0
Thus digest[1] = 0.

Write a function answer(digest) that takes an array of 16 integers and returns another array of 16 that correspond to
the unique message that created this digest. Since each value is a single byte, the values are 0 to 255 for both message
and digest.
"""

from __future__ import division  # Not strictly necessary but good for possible Python 3 compatibility


# This doesn't really *need* to be it's own function. It's more for compartmentalization
def getmultiples(num, lowerbound, upperbound, addnum):
    """
    This function finds all the factors of 256 between two given bounds, then adds
    a supplied number
    """
    lowerfactor = lowerbound // num + 1
    upperfactor = upperbound // num + 1
    return [factor * num + addnum for factor in range(lowerfactor, upperfactor)]


def answer(digest):
    """
    Alright, let's talk math. The hashed function is, as stated above digest[i]
    = ( (129 * message[i]) ^ message[i - 1]) % 256 NOTE: '^' in python means
    bit-wise exclusive OR

    Here was my thought process: Let's make this problem a little simpler to
    start out with Let a = ((129 * message[i]) ^ message[i-1]) Alrighty then, so
    what are we left with?

    x mod 256 = digest[i]

    There are an unlimited number of solutions to the above problem. Well
    shoot...  But wait! There are constraints on what 'x' can be!  What's the
    lowest number we could get from '((129 * message[i]) ^ message[i-1])'?  Well
    the lowest value message[i] and message[i + 1] could be is 0 and 129 * 0 is
    still 0.  Thus our lower bound is, you guessed it, 0.

    Well what about an upper bound?  At most message[i] and message[i-1] could
    be 255 (11111111 in binary). Thus our upper bound is 255 * 129 (it says 256
    * 129 below which is an error. The program still gets the correct solution
    though)

    Now then, we know that 'x mod 256 = digest[i]' means 'the remainder of x
    divided by 256 is digest[i]' right?  So in other words (according to the
    division theorem which states that any number 'a' can be expressed as 'bq +
    r' b and q are two quotients and r is the remainder) x = 256q + digest[i].

    So then, let's find all multiples of 256 between our bounds and add digest[i]
    to them.

    Awesome! That gives us a very long list of possible values for x but at
    least it's a finite number!

    Alrighty then, before we go much further, let's talk about bit-wise XOR.
    Basically the only thing one needs to know in terms of this problem can be
    expressed thusly:
    a XOR b = c
    b XOR a = c
    c XOR b = a
    c XOR a = b
    So not only is XOR communitive, but it is also it's own inverse operation.
    It undoes itself.

    This means that since for any message[i] we will also know message[i-1] we
    can easily narrow down that long list of possible values of x. Since ((129 *
    message[i]) XOR message[i-1]) = x, it can also be stated that message[i-1]
    XOR x = 129 * message[i]. Which also means that:

    (message[i-1] XOR x)/129 = message[i]

    Since we know that message[i] is a whole number, that means that
    message[i-1] XOR x must be divisible by 129. Or, expressed as a modular
    arithmatic expression:

    (message[i-1] XOR x) mod 129 = 0

    So then, let's just go through and find all of the possible values for x
    that when XORed with the previous message character are divisable by 129.
    When we XOR it with message[i-1] and divide it by 129. Also, since we know
    these messages must be less than a byte each, we also need to convert it to
    mod 256.

    Fin


    """
    message = []
    for charnum in range(len(digest)):
        if charnum == 0:
            prevcharnum = 0
        else:
            prevcharnum = message[charnum - 1]
        for multiple in getmultiples(256, 0, 256*129, digest[charnum]):
            if (multiple ^ prevcharnum) % 129 == 0:
                message.append(((multiple ^ prevcharnum) // 129) % 256)
    return message
