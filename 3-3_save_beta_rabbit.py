"""
Save Beta Rabbit
================

Oh no! The mad Professor Boolean has trapped Beta Rabbit in an NxN grid of rooms. In the center of each room (except for
the top left room) is a hungry zombie. In order to be freed, and to avoid being eaten, Beta Rabbit must move through
this grid and feed the zombies.

Beta Rabbit starts at the top left room of the grid. For each room in the grid, there is a door to the room above,
below, left, and right. There is no door in cases where there is no room in that direction. However, the doors are
locked in such a way that Beta Rabbit can only ever move to the room below or to the right. Once Beta Rabbit enters a
room, the zombie immediately starts crawling towards him, and he must feed the zombie until it is full to ward it off.
Thankfully, Beta Rabbit took a class about zombies and knows how many units of food each zombie needs be full.

To be freed, Beta Rabbit needs to make his way to the bottom right room (which also has a hungry zombie) and have used
most of the limited food he has. He decides to take the path through the grid such that he ends up with as little food
as possible at the end.

Write a function answer(food, grid) that returns the number of units of food Beta Rabbit will have at the end, given
that he takes a route using up as much food as possible without him being eaten, and ends at the bottom right room.
If there does not exist a route in which Beta Rabbit will not be eaten, then return -1.

food is the amount of food Beta Rabbit starts with, and will be a positive integer no larger than 200.

grid will be a list of N elements. Each element of grid will itself be a list of N integers each, denoting a single row
of N rooms. The first element of grid will be the list denoting the top row, the second element will be the list
denoting second row from the top, and so on until the last element, which is the list denoting the bottom row. In the
list denoting a single row, the first element will be the amount of food the zombie in the left-most room in that row
needs, the second element will be the amount the zombie in the room to its immediate right needs and so on. The top left
room will always contain the integer 0, to indicate that there is no zombie there.

The number of rows N will not exceed 20, and the amount of food each zombie requires will be a positive integer not
exceeding 10.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) food = 7
    (int) grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
Output:
    (int) 0

Inputs:
    (int) food = 12
    (int) grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
Output:
    (int) 1
"""

def creategraph(gridlist):
    """
    This function takes a two dimensional array as input (number of columns and rows must be equal)
    The elements in the array are the out-going distances of their respective nodes
    
    Creating a graph probably isn't *really* necessary but it was a helpful abstraction for 
    me to wrap my brain around the problem.
    """
    from string import ascii_lowercase
    size = len(gridlist)
    letters = list(ascii_lowercase)[:size]
    gengraph = {}
    edge_cost = {}
    for loc in range(size):
        for num in range(size):
            node = letters[loc] + str(num)
            gengraph[node] = list()
            edge_cost[node] = gridlist[loc][num]
            if num + 1 < size:
                gengraph[node].append(letters[loc] + str(num + 1))
            if loc + 1 < size:
                gengraph[node].append(letters[loc + 1] + str(num))
    return gengraph, edge_cost


class MemoizeFunction:
    """
    This class is stolen from somewhere.
    It serves as a wrapper for the funciton.
    Before the function is run, it checks the inputs in self.memory 
    and simply returns the value if it's in there.
    """
    def __init__(self, func):
        self.function = func
        self.memory = dict()

    def __call__(self, *args):
        try:
            return self.memory[args]
        except KeyError:
            self.memory[args] = self.function(*args)
            return self.memory[args]


def answer(food, grid):
    G, distances = creategraph(grid)

    

    @MemoizeFunction
    def find_fewest_leftovers(food_supply, node):
        """
        As this function generates every possible path from top left to bottom right,
        memoization is an absolutely neccessary here.
        It starts with the bottom right node and recurses, eventually returning the
        least efficient path that fits our constraints.
        """
        if food_supply < 0:
            return 201
        if len(G[node]) == 0:
            return food_supply
        elif len(G[node]) == 1:
            node = G[node][0]
            return find_fewest_leftovers(food_supply, node)
        else:
            node1, node2 = G[node]
            return min(find_fewest_leftovers(food_supply, node1), find_fewest_leftovers(food_supply, node2))
    leftovers = find_fewest_leftovers(food, 'a0')
    return leftovers if leftovers != 201 else -1
