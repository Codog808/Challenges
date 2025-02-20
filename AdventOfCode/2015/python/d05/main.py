import re 

def is_nice(string):
    """ created by chatgpt o1-preview """ 
    vowels = set('aeiou')
    forbidden = ['ab', 'cd', 'pq', 'xy']
    vowel_count = sum(1 for char in string if char in vowels)
    if vowel_count < 3:
        return False
    
    has_double_letter = any(string[i] == string[i+1] for i in range(len(string) -1 ))
    if not has_double_letter:
        return False

    if any(sub in string for sub in forbidden):
        return False
    
    return True

def is_really_nice(string):
    """ created by chatgpt 4o """ 
    condition1 = re.search(r'(..).*\1', string)
    condition2 = re.search(r'(.).\1', string)
    return bool(condition1 and condition2)

class d05:
    def __init__(self, filename):
        self.lines = open(filename).read().strip().split('\n')

    def p1(self):
        nice_strings = []
        for string in self.lines:
            if is_nice(string):
                nice_strings.append(string)
        print("answer to part 1:", len(nice_strings))

    def p2(self):
        nice_strings = []
        for string in self.lines:
            if is_really_nice(string):
                nice_strings.append(string)
        print("answer to part2:", len(nice_strings))
def main():
    day = d05('input')
    p1 = day.p1()
    p2 = day.p2()

if __name__ == '__main__':
    main()
    
