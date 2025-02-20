from itertools import permutations

def permute(locations):
    if len(locations) == 1:
        return [locations]

    permutations = []
    for i in range(len(locations)):
        current_location = locations[i]
        remaining_locations = locations[i+1:] 
        for p in permute(remaining_locations):
            permutations.append([current_location] + p)
    return permutations

def change_each_element_to_first(locations):
    permutations = []
    for i in range(len(locations)):
        # Copy the list so you don't modify the original
        new_order = locations[i:] + locations[:i]
        yield new_order


def get_distances(routes, distances):
    for route in routes:
        print(route)
        total = 0
        for old_index, location in enumerate(route[1:]):
            total += distances[(route[old_index], location)]
        yield total



def p1(input_filename, debug=False):
    """
    * Given locations and the distances between them, find the shortest distance of travel to reach all of these locations.
    # Travelling salesmen Problem
        1. Get all the routes (permutation of routes)
        1+ Get a base-distance, compare and if route is greater than base-distance break.
        2. Calculate the distance of each route
        3. Find the shortest route
    """
    distances = {} 
    locations = set()
    for line in open(input_filename).read().strip().splitlines():
        location, distance = line.split(' = ')
        location = location.split(' to ')
        distances[tuple(location)] = int(distance.strip())
        distances[tuple(reversed(location))] = int(distance.strip())
        locations.add(location[0])
        locations.add(location[1])

    #Routes aren't constant, figure out why 10/15/24
    # Solution is found but the way to get there is erroneous 10/19/24
    #routes = permute(list(locations))
    loc = list(locations)
    routes = []
    for list_of_locations in change_each_element_to_first(loc):
        input(list_of_locations)
        routes.append([route for route in permute(list_of_locations) if len(route) == 7])
    routes = [route for list_of_routes in routes for route in list_of_routes]

    shortest_distance = float('inf')
    for distance in get_distances(routes, distances):
        if distance < shortest_distance:
            shortest_distance = distance
    if debug:
        print(distances)
        print(locations)
        print("\n\n\n")
        print(len(locations))
        print(len(routes), routes)
    # This works if you spam the output and look for the shortest distance...
    # Need to revamp how the permutations work to where it accepts 'something'...
    print("answer for part 1:", str(shortest_distance))

def chatgptp1(filename, debug=False):
    distances = {}
    cities = set()
    for line in open(filename).read().strip().split('\n'):
        two_cities, distance = line.split(" = ")
        city1, city2 = two_cities.split(' to ')
        distances[frozenset([city1, city2])] = int(distance)
        cities.update([city1, city2])
    all_routes = permutations(cities)
    shortest_distance = float('inf')
    shortest_route = None
    for route in all_routes:
        total_distance = 0
        valid_route = True
        for i in range(len(route) -1):
            leg = frozenset([route[i], route[i + 1]])
            if leg in distances:
                total_distance += distances[leg]
            else:
                valid_route = False
        if valid_route and total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_route = route

    print("PART 1:")
    print(f"The shortest route is {' -> '.join(shortest_route)} with a distance of {shortest_distance}")
    print()


def chatgptp2(filename, debug=False):
    distances = {}
    cities = set()
    for line in open(filename).read().strip().split('\n'):
        two_cities, distance = line.split(" = ")
        city1, city2 = two_cities.split(' to ')
        distances[frozenset([city1, city2])] = int(distance)
        cities.update([city1, city2])
    all_routes = permutations(cities)
    longest_distance = 0
    longest_route = None
    for route in all_routes:
        total_distance = 0
        valid_route = True
        for i in range(len(route) -1):
            leg = frozenset([route[i], route[i + 1]])
            if leg in distances:
                total_distance += distances[leg]
            else:
                valid_route = False
        if valid_route and total_distance > longest_distance:
            longest_distance = total_distance
            longest_route = route
    
    print("PART 2:")
    print(f"The longest route is {' -> '.join(longest_route)} with a distance of {longest_distance}")

if __name__ == '__main__':
    chatgptp1('input', debug=True)
    chatgptp2('input')
