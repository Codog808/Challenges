""" Day 15, 11.20.2024, Science for Hungry People """
from itertools import product

def calculate_score_p1(teaspoons, cookies):
    properties = {}
    for property in ['capacity', 'durability', 'flavor', 'texture']:
        property_score = 0
        for i, cookie_name in enumerate(cookies):
            cookie_values = cookies[cookie_name]
            value = cookie_values[property] 
            property_score += value * teaspoons[i]

        properties[property] = max(property_score, 0)
    score = 1
    for property in properties:
        score *= properties[property]
    return score

def calculate_score_p2(teaspoons, cookies):
    properties = {}
    for property in ['capacity', 'durability', 'flavor', 'texture']:
        property_score = 0
        calories = 0
        for i, cookie_name in enumerate(cookies):
            cookie_values = cookies[cookie_name]
            value = cookie_values[property] 
            property_score += value * teaspoons[i]
            calories += cookie_values['calories'] * teaspoons[i]
        properties[property] = max(property_score, 0)
        if calories != 500:
            return 0

    score = 1
    for property in properties:
        score *= properties[property]
    return score

class main:
    def __init__(self, filename, teaspoons=100, debug=False):
        self.filename = filename
        self.debug = debug
        self.teaspoons = teaspoons

    def get_input(self):

        if self.debug:
            print()
            print("\tDEBUGGING 'get_input'; Must Run within method")
            print(f"\t\tCHECKING, line from '{self.filename}'")

        cookie_types = {}
        for line in open(self.filename).read().strip().split("\n"):

            if self.debug:
                print(f"\t\t{line}")

            cookie_type_dirty, cookie_traits = line.strip().split(":")
            cookie_type = cookie_type_dirty.strip().lower()
            cookie_types[cookie_type] = {} 
            for cookie_trait_and_value in cookie_traits.strip().split(','):
                cookie_trait, trait_value = cookie_trait_and_value.strip().split(" ")
                cookie_types[cookie_type][cookie_trait] = int(trait_value)

        if self.debug:
            print("\tDONE DEBUGGING FUNCTION\n")
        return cookie_types


    def p1(self):
        """
            Cookie Recipe
                exactly 100 teaspoons of ingredients
                    pass
                Cookie ingredient Traits
                    Capacity: absorbtion of milk
                    Durability: intactability when full of milk
                    Flavor: improving taste
                    Texture: improving feeling
                    Calories: 
            
            Cookie types
                Contains the traits above
                Pass

            Given a set of 'Cookie Types' find the best mixture.
        """
        print("STARTING PART 1...")
        cookie_types = self.get_input()
        
        # SCORE IS TALLIED UP WRONGLY, 1228800000 is wrong, 11.23.24
        # REPLICATE CODE WITHIN chatgpt.py
        best_score = 0
        for amounts in product(range(101), repeat=len(cookie_types.keys())):
            if sum(amounts) == 100:
                score = calculate_score_p1(amounts, cookie_types)
                if score > best_score:
                    best_score = score
        if self.debug:
            print("\tDEBUGGING 'p1'")
            print("\t\toutputting given 'cookie_types'")
            for cookie_type in cookie_types:
                print(f"\t\t\t{cookie_type}: {cookie_types[cookie_type]}")
        print("\tBEST SCORE IS ",best_score)

    def p2(self):
        print("STARTING PART 2...")
        cookie_types = self.get_input()
        best_score = 0
        for amounts in product(range(101), repeat=len(cookie_types.keys())):
            if sum(amounts) == 100:
                score = calculate_score_p2(amounts, cookie_types)
                if score > best_score:
                    best_score = score
        print("\tPART 2: BEST SCORE IS ",best_score)

if __name__ == '__main__':
    d15 = main("input", debug=True)
    d15.p1()
    d15.p2()

