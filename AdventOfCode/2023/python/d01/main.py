import re 
class day01:
    def __init__(self, filename):
        with open(filename) as f:
            self.raw = f.read().strip().split("\n")
            f.close()
    def p1(self):
        total = 0
        for line in self.raw:
            all_digits = re.findall(r'\d', line)
            first_and_last = "".join([all_digits[0], all_digits[-1]])
            total += int(first_and_last)
        print(total)
    def p2(self):
        mapping  = {
                "one": 'one1one',
                "two": 'two2two',
                "three": 'three3three',
                "four": 'four4four',
                "five": 'five5five',
                "six" : 'six6six',
                "seven": 'seven7seven',
                "eight": 'eight8eight',
                "nine": 'nine9nine'
                }
        total = 0
        for line in self.raw:
            for key, value in mapping.items():
                line = line.replace(key, value)

            #Extract first and last digit
            first_digit = next((char for char in line if char.isdigit()), None)
            last_digit = next((char for char in reversed(line) if char.isdigit()), None)

            #Sum everything up
            if first_digit and last_digit:
                value = int(first_digit + last_digit)
                total += value

        print(total)
def main():
    day01('examp1').p1()
    puz = day01('puzzle')
    puz.p1()
    day01('examp2').p2()
    puz.p2()
    # this output is erroneous.
main()
        

