"""
When it rains it pours
======================

It's raining, it's pouring. You and your agents are nearing the building where the captive rabbits are being held, but a
sudden storm puts your escape plans at risk. The structural integrity of the rabbit hutches you've built to house the
fugitive rabbits is at risk because they can buckle when wet. Before the rabbits can be rescued from Professor Boolean's
lab, you must compute how much standing water has accumulated on the rabbit hutches.

Specifically, suppose there is a line of hutches, stacked to various heights and water is poured from the top (and
allowed to run off the sides). We'll assume all the hutches are square, have side length 1, and for the purposes of this
problem we'll pretend that the hutch arrangement is two-dimensional.

For example, suppose the heights of the stacked hutches are [1,4,2,5,1,2,3] (the hutches are shown below):

...X...
.X.X...
.X.X..X
.XXX.XX
XXXXXXX
1425123

When water is poured over the top at all places and allowed to runoff, it will remain trapped at the 'O' locations:

...X...
.XOX...
.XOXOOX
.XXXOXX
XXXXXXX
1425123

The amount of water that has accumulated is the number of Os, which, in this instance, is 5.

Write a function called answer(heights) which, given the heights of the stacked hutches from left-to-right as
a list,computes the total area of standing water accumulated when water is poured from the top and allowed to run off
the sides.

The heights array will have at least 1 element and at most 9000 elements. Each element will have a value of at least 1,
and at most 100000.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) heights = [1, 4, 2, 5, 1, 2, 3]
Output:
    (int) 5

Inputs:
    (int list) heights = [1, 2, 3, 2, 1]
Output:
    (int) 0
"""


def answer(heights):
    # Right off of the bat, water can't collect if there are fewer than 3
    # hutches
    if len(heights) < 3:
        return 0
    """
    When figuring out how to go about this program, I thought about how to
    qualify where exactly water would collect. It would collect between two
    columns assuming there doesn't exist any larger columns in between them. The
    highest the water level could possibly be is the height of the shortest
    bounding column. I'd call these columns towers. This concept was simple
    enough  The problem then arises of figuring out how to programatically
    define these towers and how best to find them.

    My initial algorithm started from the first column and would iterate through
    each column, looking for a column that was its height or taller. If it found
    one, it would add that column to the list of towers and the new tower would
    become the new standard. This worked great in certain cases, but consider
    the following configuration:

    X
    XX X
    XXXX
    3212

    My algorithm would see the first tower with a height of three and would not
    find any other columns with a height of 3 or greater. Thus it would say no
    water would accumulate and would return a value of 0.

    Well that's no good. What then?
    I kept thinking, to a human brain, it's so obvious. We can see the whole
    picture so it's easy to see the boundries between which water would
    accumulate. That's when I realized the problem with my algorithm. It only
    saw the picture from left to right.

    I added another iteration, from right to left, creating two different lists
    of towers. There was some overlap so I converted both lists to sets (set theory
    WOOOO!!) and did a union.

    Next I iterate through each tower and determine the water level by figuring
    out which is shorter, it or the following tower. Then I iterate through each
    intermediate column and add the subtraction of its height from the water
    level to the total score.

    """
    primtowers = [(0, heights[0])]
    ultowers = [(len(heights) - 1, heights[-1])]
    for primcolumn in range(len(heights) - 1):
        if heights[primcolumn] >= primtowers[-1][1]:
            primtowers.append((primcolumn, heights[primcolumn]))
    for ulcolumn in range(len(heights) - 1, 0, -1):
            if heights[ulcolumn] > ultowers[-1][1]:
                ultowers.append((ulcolumn, heights[ulcolumn]))
    towers = sorted(list(set(primtowers) | set(ultowers)))
    score = 0
    for column in range(len(towers) - 1):
        try:
            towerdiff = range(towers[column][0] + 1, towers[column + 1][0])
            waterlevel = min(towers[column][1], towers[column + 1][1])
        except IndexError:
            break
        for column in towerdiff:
            score += waterlevel - heights[column]
    return score
