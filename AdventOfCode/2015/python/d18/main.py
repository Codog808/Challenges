import time
import copy
"""

Advent of Code

    [About][Events][Shop][Settings][Log Out]

Cody Shitagi 34*
      /*2015*/

    [Calendar][AoC++][Sponsors][Leaderboard][Stats]

--- Day 18: Like a GIF For Your Yard ---

After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

1B5...
234...
......
..123.
..8A4.
..765.

The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

    A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
    A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.

All of the lights update simultaneously; they all consider the same current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......

After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?

To begin, get your puzzle input.

Answer:

You can also [Shareon Bluesky Twitter Mastodon] this puzzle.

--- Part Two ---

You flip the instructions over; Santa goes on to point out that this is all just an implementation of Conway's Game of Life. At least, it was, until you notice that something's wrong with the grid of lights you bought: four lights, one in each corner, are stuck on and can't be turned off. The example above will actually run like this:

Initial state:
##.#.#
...##.
#....#
..#...
#.#..#
####.#

After 1 step:
#.##.#
####.#
...##.
......
#...#.
#.####

After 2 steps:
#..#.#
#....#
.#.##.
...##.
.#..##
##.###

After 3 steps:
#...##
####.#
..##.#
......
##....
####.#

After 4 steps:
#.####
#....#
...#..
.##...
#.....
#.#..#

After 5 steps:
##.###
.##..#
.##...
.##...
#.#...
##...#

After 5 steps, this example now has 17 lights on.

In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state, how many lights are on after 100 steps?


"""


import argparse

parser = argparse.ArgumentParser(description="d18, verbosity flag")
parser.add_argument('-verbose', action="store_true", help="enable verbosity")
args = parser.parse_args()

class d18:
    def __init__(self, filename):
        self.input = open(filename).read().strip().splitlines()
        self.grid = []
        for line in self.input:
            row = [True if character == "#" else False for character in line.strip()]
            self.grid.append(row)
        self.p1_grid = copy.deepcopy(self.grid)
        self.p2_grid = copy.deepcopy(self.grid)

    def p1_count_neighbors(self, row, column):
        on_count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                rr = row + dr
                cc = column + dc
                if 0 <= rr < len(self.p1_grid) and 0 <= cc < len(self.p1_grid[row]):
                    if self.p1_grid[rr][cc]:
                        on_count += 1
        return on_count

    def p1(self):
        if args.verbose:
            print("Starting Part 1...")
            print("\tPREFORMING the animation...")
        
        width_of_grid = len(self.p1_grid[0])
        length_of_grid = len(self.p1_grid)
        for animation_step in range(100):
            print("\t\tAnimation step:", animation_step)
            new_grid = [[False] * width_of_grid for _ in range(length_of_grid)]
            for row in range(length_of_grid):
                for column in range(width_of_grid):
                    on_count = self.p1_count_neighbors(row, column)
                    if self.p1_grid[row][column]:
                        if on_count in (2,3):
                            new_grid[row][column] = True
                        else:
                            new_grid[row][column] = False
                    else:
                        if on_count == 3:
                            new_grid[row][column] = True
                        else:
                            new_grid[row][column] = False

            self.p1_grid = new_grid
        print("\tDONE WITH THE STEPS...")
        total = 0
        for row in self.p1_grid:
            for element in row:
                if element:
                    total += 1
        print("\tPart 1 Answer: How many lifghts are on after 100 steps:", total)
    def p2_count_neighbors(self, row, column):
        on_count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                rr = row + dr
                cc = column + dc
                if 0 <= rr < len(self.p2_grid) and 0 <= cc < len(self.p2_grid[row]):
                    if self.p2_grid[rr][cc]:
                        on_count += 1
        return on_count

    def p2(self):
        if args.verbose:
            print("Starting Part 2...")
            print("\tPREFORMING the animation...")
        
        width_of_grid = len(self.p2_grid[0])
        length_of_grid = len(self.p2_grid)

        for animation_step in range(100):
            print("\t\tAnimation step:", animation_step)
            new_grid = [[False] * width_of_grid for _ in range(length_of_grid)]
            for row in range(length_of_grid):
                for column in range(width_of_grid):
                    on_count = self.p2_count_neighbors(row, column)
                    if self.p2_grid[row][column]:
                        if on_count in (2,3):
                            new_grid[row][column] = True
                        else:
                            new_grid[row][column] = False
                    else:
                        if on_count == 3:
                            new_grid[row][column] = True
                        else:
                            new_grid[row][column] = False

            self.p2_grid = new_grid
            self.p2_grid[0][0] = True
            self.p2_grid[len(self.grid) - 1][0] = True
            self.p2_grid[0][len(self.grid) - 1] = True
            self.p2_grid[len(self.grid) - 1][len(self.grid[0]) - 1] = True
        print("\tDONE WITH THE STEPS...")
        total = 0
        for row in self.p2_grid:
            for element in row:
                if element:
                    total += 1
        print("\tPart 2 Answer: How many lifghts are on after 100 steps:", total)

if __name__ == '__main__':
    d = d18("input")
    d.p1()
    d.p2()
