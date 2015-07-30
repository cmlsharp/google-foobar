"""
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


def getmultiples(num, lowerbound, upperbound, addnum):
    # int() is only necessary because of __future__ import.
    # This is default behavior in Python 2 but compatibility is nice
    lowerfactor = int(lowerbound / num + 1)
    upperfactor = int(upperbound / num + 1)
    return [factor * num + addnum for factor in range(lowerfactor, upperfactor)]


def answer(digest):
    message = []
    for charnum in range(len(digest)):
        if charnum == 0:
            prevcharnum = 0
        else:
            prevcharnum = message[charnum - 1]
        for multiple in getmultiples(256, 0, 256*129, digest[charnum]):
            if (multiple ^ prevcharnum) % 129 == 0:
                message.append(int((multiple ^ prevcharnum)/129) % 256)
    return message
