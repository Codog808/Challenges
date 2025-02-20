import re

def parse_input(filename):
    for line in open(filename):
        yield list(map(int, re.findall(r'\d+', line)))


def p1(filename, given_time):
    """ Figure out which reindeer is the fastest 
    1. Reindeer has two states: Flying, resting
    2. After a set time decide who is the fastest by how far they traveled
        within this set time the reindeers would iterate between flying and resting
    """
    furthest_distance = 0
    for km_s, km_time, rest_time in parse_input(filename):
        total_bursts = given_time // (rest_time + km_time)
        distance = (km_s * km_time) * total_bursts
        remaining_time = given_time % (rest_time + km_time)
        distance += min(remaining_time, km_time) * km_s
        if furthest_distance < distance:
            furthest_distance = distance
    print("Answer to part 1:", furthest_distance) 

class zeindeer:
    def __init__(self, name, km_s, km_time, rest_time):
        self.name = name
        self.km_s = km_s
        self.km_time = km_time
        self.rest_time = rest_time
        self.distance = 0
        self.points = 0
        self.rest = 0
        self.go = 0

def parse_input_p2(filename):
    for line in open(filename):
        yield {line.split(" ")[0]: list(map(int, re.findall(r'\d+', line)))}

def p2_V2(filename, race_duration=2503):
    reindeers = []
    for deer in parse_input_p2(filename):
        name = list(deer.keys())[0]
        km_s, km_time, rest_time = list(deer.values())[0]
        reindeer = zeindeer(name, km_s, km_time, rest_time)
        reindeers.append(reindeer)
    for second in range(1, race_duration + 1):
        for r in reindeers:
            cycle_time = r.km_time + r.rest_time
            full_cycles, remaining_time = divmod(second, cycle_time)
            flying_time = full_cycles * r.km_time + min(remaining_time, r.km_time)
            r.distance = flying_time * r.km_s
        lead_distance = max(r.distance for r in reindeers)
        for r in reindeers:
            if r.distance == lead_distance:
                r.points += 1

    highest_reindeer = max(r.points for r in reindeers)
    print("Answer for part 2:", highest_reindeer)




def p2_V1(filename, race_duration=2503):
    """
    Scoring System:
        1. End of Each second reward the reindeer in the lead 1 point, if it is a tie reward all tied.
    THE ANSWER IS TOO LOW, idk why. 11/13/24
    """
    reindeers = []
    for deer in parse_input_p2(filename):
        name = list(deer.keys())[0]
        km_s, km_time, rest_time = list(deer.values())[0]
        reindeer = zeindeer(name, km_s, km_time, rest_time)
        reindeers.append(reindeer)
    for second in range(1, race_duration + 1):
        print("SECOND", second)
        for reindeer in reindeers:
            if reindeer.rest > 0:
                reindeer.rest -= 1
            if reindeer.rest == 0 and reindeer.go == 0:
               reindeer.go = reindeer.km_time
            if reindeer.go > 0:
                reindeer.distance += reindeer.km_s
                reindeer.go -= 1
            if reindeer.rest == 0 and reindeer.go == 0:
               reindeer.rest = reindeer.rest_time
        max_distance = max(reindeer.distance for reindeer in reindeers)
        for reindeer in reindeers:
            if reindeer.distance == max_distance:
                reindeer.points += 1
    max_points = max(reindeer.points for reindeer in reindeers)
    print("Answer for part 2:", max_points)

             

def p2_chatgpt(filename, race_duration=2503):
    """
    Put some genuine time into this... 11/11/24
    Not Working 11/13/24
        """
    reindeers = [deer for deer in parse_input_p2(filename)]
    distances = {str(next(iter(deer))): 0 for deer in reindeers}
    points = {str(next(iter(deer))): 0 for deer in reindeers}
    for second in range(1, race_duration + 1):
        for reindeer in reindeers:
            km_s, km_time, rest_time = reindeer[str(next(iter(reindeer)))]
            cycle_time = km_time + rest_time
            time_in_cycle = second % cycle_time
            if time_in_cycle > 0 and time_in_cycle <= km_s:
                distances[str(next(iter(reindeer)))] += km_s
        
        lead = [("blank", 0)]
        for reindeer in reindeers:
            distance = distances[str(next(iter(reindeer)))]
            if lead[0][-1] < distance:
                lead = [(str(next(iter(reindeer))), distance)]

            elif lead[0][-1] == distance:
                lead.append((str(next(iter(reindeer))), distance))

        for l in lead:
            points[l[0]] += l[-1]
    max_points = max(points.values())
    print(max_points)



if __name__ == '__main__':
    p1("input", 2503)
    p2_V2('input')
