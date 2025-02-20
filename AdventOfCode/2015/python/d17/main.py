from itertools import combinations

def combinations_from_scratch(lst, r):
    if r == 0:
        return [[]]

    if len(lst) < r:
        return []
    
    first = lst[0]
    with_first = []
    for combo in combinations_from_scratch(lst[1:],r -1):
        with_first.append([first] + combo)

    without_first = combinations_from_scratch(lst[1:], r)
    return with_first + without_first

class d17:
    """
    --- Day 17: No Such Thing as Too Much ---

The elves bought too much eggnog again - 150 liters this time. To fit it all into 
your refrigerator, you'll need to move it into smaller containers. 
You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. 
If you need to store 25 liters, there are four ways to do it:

    15 and 10
    20 and 5 (the first 5)
    20 and 5 (the second 5)
    15, 5, and 5

Filling all containers entirely, how many different 
combinations of containers can exactly fit all 150 liters of eggnog?

    """
    def __init__(self, filename):
        self.containers = list(map(int, open(filename).read().strip().splitlines()))
        self.p1_target = 150
        
    def chatgpt_p1(self):
        TARGET = 150

# Find all combinations of containers that sum to the target
        valid_combinations = []
        for r in range(1, len(self.containers) + 1):
            for combo in combinations_from_scratch(self.containers, r):
                if sum(combo) == TARGET:
                    valid_combinations.append(combo)
        print("Part 1 Answer:", len(valid_combinations))
        return valid_combinations
    def chatgpt_p2(self):
        valid_combinations = self.chatgpt_p1()

# Determine the minimum number of self.containers used among all valid combinations
        min_length = min(len(c) for c in valid_combinations)

# Count how many valid combinations use that minimum number of self.containers
        count_min_length = sum(1 for c in valid_combinations if len(c) == min_length)

        print("Minimum number of self.containers used:", min_length)
        print("Number of ways to use that many containers:", count_min_length)

if __name__ == "__main__":
    d = d17("input")
    ways = d.chatgpt_p1()
    d.chatgpt_p2()

