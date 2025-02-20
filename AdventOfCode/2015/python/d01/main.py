class day01:
    def __init__(self, filename):
        with open(filename) as f:
            self.floor_instructions = f.read().strip()
    def part1(self):
        up = 0
        down = 0
        for floor_type in self.floor_instructions:
            if floor_type == "(":
                up += 1
            else:
                down += 1
        print(up - down, "\tfrom floor 0")
    def part2(self):
        up = 0
        down = 0
        for floor_type in self.floor_instructions:
            if floor_type == "(":
                up += 1
            else:
                down += 1

            if down > up:
                print(down + up, '\twhen santa enters the basement')
                break

day01("input").part1()
day01("input").part2()
