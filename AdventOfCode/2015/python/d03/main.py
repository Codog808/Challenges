class d03:
    def __init__(self, filename):
        self.input = open(filename).read().strip()
    def p1(self):
        north = 0
        west = 0
        houses_visited = {}
        for characters in self.input:
            if (north, west) in houses_visited:
                houses_visited[(north,west)] += 1
            else:
                houses_visited[(north, west)] = 1

            if characters == '^':
                north += 1
            elif characters == 'v':
                north -= 1
            elif characters == '>':
                west += 1
            elif characters == '<':
                west -= 1

        # 9/10: Answer is too low.
        # 9/11: fixed, didn't include the starting point
        print(len(houses_visited))
    def p2(self):
        north0 = 0
        west0 = 0
        north1 = 0
        west1 = 0
        houses_visited = {}
        for pair_index in range(len(self.input) // 2):
            if (north0, west0) in houses_visited:
                houses_visited[(north0,west0)] += 1
            else:
                houses_visited[(north0, west0)] = 1
            if (north1, west1) in houses_visited:
                houses_visited[(north1,west1)] += 1
            else:
                houses_visited[(north1, west1)] = 1
            
            santa = self.input[pair_index * 2]
            robo_santa = self.input[pair_index * 2 + 1]

            if santa == '^':
                north0 += 1
            elif santa == 'v':
                north0 -= 1
            elif santa == '>':
                west0 += 1
            elif santa == '<':
                west0 -= 1
            if robo_santa == '^':
                north1 += 1
            elif robo_santa == 'v':
                north1 -= 1
            elif robo_santa == '>':
                west1 += 1
            elif robo_santa == '<':
                west1 -= 1
        print(len(houses_visited))

if __name__ == '__main__':
    puzzle = d03('input')
    puzzle.p1()
    puzzle.p2()

