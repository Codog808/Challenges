import pandas as pd
import math
from io import StringIO

def make_item_shop():
    item_shop = {}
    stringed_item_shop = open("item.shop").read().strip()
    for section in stringed_item_shop.split("\n\n"):
        lines = section.strip().splitlines()
        category = lines[0].split(":")[0]
        columns = ["Name", "Cost", "Damage", "Armor"]
        data = pd.read_csv(
            StringIO("\n".join(lines[1:])),
            sep='\s+',
            names=columns
        )
        item_shop[category] = data.to_dict(orient="records")

    item_shop["Armor"].append({"Name": None, "Cost": 0, "Damage":0, "Armor": 0})
    return item_shop

def make_boss():
    boss = {}
    for line in open("boss.stats").read().strip().splitlines():
        key, value = line.split(": ")
        boss[key] = int(value)
    return boss

def combinatorics_combinations(arrangement, r):
    if r == 0:
        return [[]]
    if len(arrangement) < r:
        return []
    with_first = combinatorics_combinations(arrangement[1:], r - 1)
    with_first = [[arrangement[0]] + comb for comb in with_first]
    without_first = combinatorics_combinations(arrangement[1:], r)
    return with_first + without_first


def all_combinations():
    item_shop = make_item_shop()
    for weapon in item_shop['Weapons']:
        for armor in item_shop['Armor']:
            for ring_count in range(3):
                ring_combos = combinatorics_combinations(item_shop['Rings'], ring_count)
                for ring_selection in ring_combos:
                    setup = [weapon, armor] + ring_selection
                    yield setup

    
def does_player_win(player_hp, player_damage, player_armor):
    boss = make_boss()
    player_damage_to_boss = max(1, player_damage - boss['Armor'])
    boss_damage_to_player = max(1, boss['Damage'] - player_armor)

    player_turns_to_die = int(math.ceil(player_hp / boss_damage_to_player))
    boss_turns_to_die = int(math.ceil(boss['Hit Points'] / player_damage_to_boss))
    return player_turns_to_die >= boss_turns_to_die 

def answers():
    min_cost = float("inf")
    max_cost = 0
    for setup in all_combinations():
        total_cost = sum(item['Cost'] for item in setup)
        total_damage = sum(item['Damage'] for item in setup)
        total_armor = sum(item['Armor'] for item in setup)
        if does_player_win(100, total_damage, total_armor):
            min_cost = min(min_cost, total_cost)
        else:
            max_cost = max(max_cost, total_cost)
    print("Answer for part 1:", min_cost, "Is it minimum cost to win.")
    print("Answer for part 2:", max_cost, "Is it maximum cost to win.")


if __name__ == '__main__':
    answers()
    pass
