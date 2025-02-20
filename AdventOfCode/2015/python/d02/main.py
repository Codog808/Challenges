import math
    
class day02:
    def __init__(self, filename):
        with open(filename) as f:
            self.expressions = [list(map(int, expression.strip().split("x"))) for expression in f.read().strip().split("\n")]
    def part1(self):
        total_wrapping_paper = 0
        for expression in self.expressions:
            top_bottom = 2 * expression[0] * expression[1]
            front_back = 2 * expression[1] * expression[2]
            right_left = 2 * expression[2] * expression[0]
            slack = min([top_bottom, front_back, right_left]) // 2
            #print(expression)
            #print(top_bottom)
            #print(front_back)
            #print(right_left)
            #print(slack)
            total_wrapping_paper += slack + top_bottom + front_back + right_left
        print("total square feet of wrapping paper:", total_wrapping_paper)
    def part2(self):
        total_ribbon = 0
        for expression in self.expressions:
            a, b = sorted(expression)[:2]
            volume = math.prod(expression)
            total_ribbon += (a * 2) + (b * 2) + volume
        print("total ribbon required:", total_ribbon)



day02('input').part1()
day02('input').part2()
