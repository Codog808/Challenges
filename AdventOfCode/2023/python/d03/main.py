def is_symbol(char):
    return char not in '0123456789.'
def is_adjacent_to_symbol(schematic, row, col, left_bound, right_bound):
    """Check if the number is adjacent to a symbol."""
    for row_offset in range(-1, 2):
        for col_offset in range(-1, 2):
            for index in range(left_bound, right_bound + 1):
                adj_row = row + row_offset
                adj_col = col + col_offset + index - left_bound
                if 0 <= adj_row < len(schematic) and 0 <= adj_col < len(schematic[0]):
                    if is_symbol(schematic[adj_row][adj_col]):
                        return True
    return False

class d03:
    def __init__(self, filename):
        self.lines = open(filename).read().strip().split('\n')
    def p1(self):
        total = 0
        visited = set() 
        for row in range(len(self.lines)):
            cols = []
            num = 0
            stop = False
            for col in range(len(self.lines[row])):
                focus = self.lines[row][col]
                if focus.isdigit():
                    num = num * 10 + int(focus) 
                    cols.append(col)
                    visited.add((row, col))
                    if not stop:
                        stop = True
                elif stop:
                    left_bound = cols[0]
                    start_col = cols[0]
                    if left_bound - 1 >= 0:
                        left_bound -= 1
                    right_bound = cols[-1]
                    if right_bound + 1 <= len(self.lines[row]):
                        right_bound += 1
                    if is_adjacent_to_symbol(self.lines, row, start_col, left_bound, right_bound):
                        total += num
                    cols = []
                    num = 0
                    stop = False
        print(total)


def main():
    ex = d03('example')
    ex.p1()
    inp = d03('input')
    inp.p1()
main()

