import re
from collections import defaultdict

def parse_input(data):
    reindeer = []
    pattern = r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
    for line in data.splitlines():
        match = re.match(pattern, line)
        if match:
            name, speed, fly_time, rest_time = match.groups()
            reindeer.append({
                "name": name,
                "speed": int(speed),
                "fly_time": int(fly_time),
                "rest_time": int(rest_time),
            })
    return reindeer

def simulate_race(reindeer, total_time):
    distances = {r["name"]: 0 for r in reindeer}
    points = defaultdict(int)
    
    for t in range(1, total_time + 1):
        # Calculate distances for all reindeer at time `t`
        for r in reindeer:
            ### COdy: So flying time is found by getting full_cycles past 
            ### (which is a divmod of current time, t, by cycle time)
            ### and then the mod of that operation is remaining_time.
            ### check and see if remaning time exceeds fly_time, therefore it is rest 09:35
            ###     this check is by picking the smallest value between remaining time and the constant 'fly_time'
            ### gneius, thank you chatgpt.:w
            cycle_time = r["fly_time"] + r["rest_time"]
            full_cycles, remaining_time = divmod(t, cycle_time)
            flying_time = full_cycles * r["fly_time"] + min(remaining_time, r["fly_time"])
            distances[r["name"]] = flying_time * r["speed"]
        
        # Determine the lead distance
        lead_distance = max(distances.values())
        
        # Award points to all reindeer in the lead
        for name, distance in distances.items():
            if distance == lead_distance:
                points[name] += 1
    
    return points

# Example Input

# Parse input and simulate race
reindeer = parse_input(open("input").read())
points = simulate_race(reindeer, 2503)

# Find the winner
winner = max(points, key=points.get)
print(f"The winning reindeer is {winner} with {points[winner]} points.")

