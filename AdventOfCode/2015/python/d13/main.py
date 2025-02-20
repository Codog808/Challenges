def map_happiness(file_about_happiness_arrangement):
    arrangement_map = {}
    for line in open(file_about_happiness_arrangement).read().strip().split("\n"):
        x = line.split(" ")
        focus = x[0]
        arthimetic = x[2]
        value = int(x[3])
        antifocus = x[-1][:-1]
        if focus not in arrangement_map:
            arrangement_map[focus] = {}
        arrangement_map[focus][antifocus] = {arthimetic: value}
    return arrangement_map
        
def my_permutations(elements):
    # permutation = n!
    if len(elements) <= 1:
        return [elements]
    
    all_perms = []
    for i in range(len(elements)):
        current = elements[i]
        remaining_elements = elements[:i] + elements[i+1:]
        for perm in my_permutations(remaining_elements):
            all_perms.append([current] + perm)
    return all_perms

def calculate_happiness(arrangement, arrangement_map):
    total_happiness = 0
    guest_num = len(arrangement)
    # calculate the happiness of the entire arrangement
    for i in range(guest_num):
        person_focus = arrangement[i]
        person_next = arrangement[(i + 1) % guest_num]
        focus_value = arrangement_map[person_focus][person_next]
        focus_op = tuple(focus_value.keys())[0]
        if focus_op == "gain":
            total_happiness += focus_value[focus_op]
        else:
            total_happiness -= focus_value[focus_op]

        next_value = arrangement_map[person_next][person_focus]
        next_op = tuple(next_value.keys())[0]
        if next_op == "gain":
            total_happiness += next_value[next_op]
        else:
            total_happiness -= next_value[next_op]
    return total_happiness



def p1(arrangement_map, guest_permutations):
    total = 0
    for permutation in guest_permutations:
        total_arrangement = calculate_happiness(permutation, arrangement_map)
        if total_arrangement > total:
            total = total_arrangement
    print("Answer to part 1:", total)
    return total

def p2():
    """
    From the guest list of 8 people add yourself.

    1. add yourself, you give give a score of 0.
    2. implement part 1's operation (maybe segregate the finding of total)
    """
    pass
if __name__ == '__main__':
    file_about_happiness_arrangement = 'input'
    p1_arrangement_map = map_happiness(file_about_happiness_arrangement)
    p1_guests = list(p1_arrangement_map.keys())
    p1_permutations = my_permutations(p1_guests)
    p1(p1_arrangement_map, p1_permutations)


    p1_arrangement_map['You'] = {}
    for p2_guest in p1_guests:
        if p2_guest not in p1_arrangement_map["You"]:
            p1_arrangement_map['You'][p2_guest] = {"gain": 0}  
        p1_arrangement_map[p2_guest]['You'] = {"gain": 0}  
    p1_guests.append('You')
    #input(p1_arrangement_map)
    p2_permutations = my_permutations(p1_guests)
    p1(p1_arrangement_map, p2_permutations)

