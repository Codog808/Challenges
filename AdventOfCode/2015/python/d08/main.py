class d08:
    def __init__(self, filename):
        self.lines = open(filename).read().strip().split('\n')
        self.literals = {'\\\\', '\\"', '\\x'}
    def p1(self):
        total = 0
        for line in self.lines:
            # inspired by https://medium.com/@ghaiklor/advent-of-code-2015-explanation-aa9932db6d6f#e486
            # "inspiration is a cool way of saying 'copying differently'"
            total += len(line) - len(eval(line))
        print(total)
    def p2(self):
        """ encode each line/code-representation as a new string 
            characters like " or /xxx are given an extra two characters prefixed.
            "" => "\"\""
            "aaa\aaa" = > "\"aaa\\\aaa\""
            it is looking for double-quotes and back-slashes and replacing them with itself plus two characters.
            * The total numbers of newly-encoded-strings minus number of characters-from-original-string.
        """
        total = 0
        for line in self.lines:
            # 10/13/24, the total is wrong. Find another way to parse the string properly.
            encoded_line = line.replace('\\', '\\\\').replace('"', '\\"')
            total += len('"' + encoded_line + '"') - len(line)
        print(total)
if __name__ == '__main__':
    d = d08('input')
    d.p1()
    d.p2()
