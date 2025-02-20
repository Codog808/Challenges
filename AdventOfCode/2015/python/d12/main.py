import json

def add_values(json_string):
    total = 0

    if type(json_string) == dict:
        total += sum((add_values(json_string[key]) for key in json_string.keys()))
    elif type(json_string) == list:
        total += sum((add_values(element) for element in json_string))
    if type(json_string) == int:
        return json_string
    elif type(json_string) == str:
        return 0
    return total
        

def p1(json_filename):
    total = 0
    
    total += add_values(json.loads(open(json_filename).read()))
    print("answer to part 1:", total)
    return total 

def add_values2(json_string):
    total = 0

    if type(json_string) == dict:
        if "red" in json_string.values():
            return 0
        total += sum((add_values2(json_string[key]) for key in json_string.keys()))
    elif type(json_string) == list:
        total += sum((add_values2(element) for element in json_string))
    if type(json_string) == int:
        return json_string
    elif type(json_string) == str:
        return 0
    return total

if __name__ == '__main__':
    p1('input')
    p2 = add_values2(json.loads(open('input').read()))
    print(p2)
