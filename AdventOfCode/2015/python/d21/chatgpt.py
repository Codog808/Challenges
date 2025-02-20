from itertools import combinations

# Boss stats (replace with your puzzle input)
boss_hp = 104
boss_damage = 8
boss_armor = 1

# Shop items
weapons = [
    ("Dagger", 8, 4, 0),
    ("Shortsword", 10, 5, 0),
    ("Warhammer", 25, 6, 0),
    ("Longsword", 40, 7, 0),
    ("Greataxe", 74, 8, 0),
]
armor = [
    ("None", 0, 0, 0),
    ("Leather", 13, 0, 1),
    ("Chainmail", 31, 0, 2),
    ("Splintmail", 53, 0, 3),
    ("Bandedmail", 75, 0, 4),
    ("Platemail", 102, 0, 5),
]
rings = [
    ("None", 0, 0, 0),
    ("Damage +1", 25, 1, 0),
    ("Damage +2", 50, 2, 0),
    ("Damage +3", 100, 3, 0),
    ("Defense +1", 20, 0, 1),
    ("Defense +2", 40, 0, 2),
    ("Defense +3", 80, 0, 3),
]

# Function to simulate a fight
def fight(player_hp, player_damage, player_armor, boss_hp, boss_damage, boss_armor):
    player_effective_damage = max(1, player_damage - boss_armor)
    boss_effective_damage = max(1, boss_damage - player_armor)
    
    player_turns_to_win = (boss_hp + player_effective_damage - 1) // player_effective_damage
    boss_turns_to_win = (player_hp + boss_effective_damage - 1) // boss_effective_damage
    
    return player_turns_to_win <= boss_turns_to_win

# Generate all item combinations
max_cost = 0
for weapon in weapons:
    for arm in armor:
        for ring_combo in combinations(rings, 2):
            items = [weapon, arm] + list(ring_combo)
            cost = sum(item[1] for item in items)
            damage = sum(item[2] for item in items)
            defense = sum(item[3] for item in items)
            
            if not fight(100, damage, defense, boss_hp, boss_damage, boss_armor):
                max_cost = max(max_cost, cost)

print(f"Most gold spent and still lose: {max_cost}")

