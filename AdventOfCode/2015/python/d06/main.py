def light_options(setting, start_pair, end_pair, switches):
    if setting == 'turn on':
        for y in range(start_pair[1], end_pair[1] + 1):
            for x in range(start_pair[0], end_pair[0] + 1):
                switches[(x, y)] = True
    elif setting == 'turn off':
        for y in range(start_pair[1], end_pair[1] + 1):
            for x in range(start_pair[0], end_pair[0] + 1):
                switches[(x, y)] = False
    elif setting == 'toggle':
        for y in range(start_pair[1], end_pair[1] + 1):
            for x in range(start_pair[0], end_pair[0] + 1):
                if (x, y) in switches:
                    switches[(x, y)] = not switches[(x, y)] 
                else:
                    switches[(x, y)] = True


def light_brightness(setting, start_pair, end_pair, switches):
    if setting == 'turn on':
        for y in range(start_pair[1], end_pair[1] + 1):
            for x in range(start_pair[0], end_pair[0] + 1):
                try:
                    switches[(x, y)] += 1
                except:
                    switches[(x, y)] = 1
    elif setting == 'turn off':
        for y in range(start_pair[1], end_pair[1] + 1):
            for x in range(start_pair[0], end_pair[0] + 1):
                try:
                    if switches[(x, y)] == 0:
                        continue
                    else:
                        switches[(x, y)] -= 1

                except:
                    switches[(x, y)] = 0
    elif setting == 'toggle':
        for y in range(start_pair[1], end_pair[1] + 1):
            for x in range(start_pair[0], end_pair[0] + 1):
                try:
                    switches[(x, y)] += 2
                except:
                    switches[(x, y)] = 2

class d06:
    def __init__(self, filename):
        self.lines = open(filename).read().strip().split("\n")
    def p1(self):
        settings = ['toggle', 'turn off', 'turn on']
        switches = {}
        for line in self.lines:
            for setting in settings:
                if setting in line:
                    start_pair, end_pair = line.split('through')
                    #print(start_pair, end_pair)
                    start_pair = tuple(map(int, start_pair.strip().split(' ')[-1].strip().split(',')))
                    end_pair = tuple(map(int, end_pair.strip().split(',')))
                    light_options(setting, start_pair, end_pair, switches)
        count = 0
        for key in switches:
            if switches[key]:
                count += 1
        print(count)
    def p2(self):
        settings = ['toggle', 'turn off', 'turn on']
        switches = {}
        for line in self.lines:
            for setting in settings:
                if setting in line:
                    start_pair, end_pair = line.split('through')
                    #print(start_pair, end_pair)
                    start_pair = tuple(map(int, start_pair.strip().split(' ')[-1].strip().split(',')))
                    end_pair = tuple(map(int, end_pair.strip().split(',')))
                    light_brightness(setting, start_pair, end_pair, switches)
        
        count = sum(switches[key] for key in switches)
        print(count)


if __name__ == '__main__':
    day = d06('input')
    day.p1()
    day.p2()


