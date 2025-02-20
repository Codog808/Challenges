import itertools

def parse_input(input_string):
    ingredients = {}
    for line in input_string.strip().split('\n'):
        name, properties = line.split(': ')
        props = {}
        for prop in properties.split(', '):
            key, value = prop.split(' ')
            props[key] = int(value)
        ingredients[name] = props
    return ingredients

def calculate_score(ingredients, amounts):
    total_props = {}
    for prop in ['capacity', 'durability', 'flavor', 'texture']:
        total = 0
        for i, ingredient in enumerate(ingredients):
            total += amounts[i] * ingredients[ingredient][prop]
            ## PERSONAL PROBLEM WAS IN THE calculate_score
        total_props[prop] = max(total, 0)
    score = 1
    for prop in total_props:
        score *= total_props[prop]
    return score

def find_best_score(ingredients):
    best_score = 0
    num_ingredients = len(ingredients)
    for amounts in itertools.product(range(101), repeat=num_ingredients):
        if sum(amounts) == 100:
            score = calculate_score(ingredients, amounts)
            if score > best_score:
                best_score = score
    return best_score

# Example usage:
#input_string = """
#Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
#Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
#"""

ingredients = parse_input(open("input").read())
best_score = find_best_score(ingredients)
print("Best score:", best_score)

