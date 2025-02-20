import heapq

# Wrapper class for state comparison based on total mana spent
class StateWrapper:
    def __init__(self, total_mana_spent, state):
        self.total_mana_spent = total_mana_spent
        self.state = state

    def __lt__(self, other):
        return self.total_mana_spent < other.total_mana_spent

# Define the boss's stats
BOSS_HIT_POINTS = 58
BOSS_DAMAGE = 9

# Define the player's initial stats
PLAYER_HIT_POINTS = 50
PLAYER_MANA = 500

# Define the spells
SPELLS = {
    'Magic Missile': {'cost': 53, 'damage': 4, 'heal': 0, 'effect': None},
    'Drain': {'cost': 73, 'damage': 2, 'heal': 2, 'effect': None},
    'Shield': {'cost': 113, 'damage': 0, 'heal': 0, 'effect': {'name': 'Shield', 'turns': 6, 'armor': 7, 'mana': 0, 'damage': 0}},
    'Poison': {'cost': 173, 'damage': 0, 'heal': 0, 'effect': {'name': 'Poison', 'turns': 6, 'armor': 0, 'mana': 0, 'damage': 3}},
    'Recharge': {'cost': 229, 'damage': 0, 'heal': 0, 'effect': {'name': 'Recharge', 'turns': 5, 'armor': 0, 'mana': 101, 'damage': 0}},
}

# Define a function to apply effects
def apply_effects(state, effects):
    new_effects = {}
    armor = 0
    mana = state['mana']
    boss_hp = state['boss_hp']
    player_hp = state['player_hp']
    for effect_name, timer in effects.items():
        if effect_name == 'Shield':
            armor += 7
        if effect_name == 'Poison':
            boss_hp -= 3
        if effect_name == 'Recharge':
            mana += 101
        timer -= 1
        if timer > 0:
            new_effects[effect_name] = timer
    return {
        'boss_hp': boss_hp,
        'mana': mana,
        'armor': armor,
        'player_hp': player_hp,
        'effects': new_effects
    }

# Define the initial state
initial_state = {
    'player_hp': PLAYER_HIT_POINTS,
    'mana': PLAYER_MANA,
    'boss_hp': BOSS_HIT_POINTS,
    'effects': {},
    'armor': 0,
    'mana_spent': 0,
    'player_turn': True  # Player starts first
}

# Use a priority queue to store states to explore
heap = []
heapq.heappush(heap, StateWrapper(0, initial_state))

# Keep track of visited states with minimal mana spent
visited = {}

min_mana_spent = float('inf')

while heap:
    wrapper = heapq.heappop(heap)
    total_mana_spent = wrapper.total_mana_spent
    state = wrapper.state

    # If we have already visited this state with less mana, skip it
    state_id = (
        state['player_hp'],
        state['mana'],
        state['boss_hp'],
        tuple(sorted(state['effects'].items())),
        state['player_turn']
    )
    if state_id in visited and visited[state_id] <= total_mana_spent:
        continue
    visited[state_id] = total_mana_spent

    # If mana spent is already higher than current minimum, skip
    if total_mana_spent >= min_mana_spent:
        continue

    # Check for win condition
    if state['boss_hp'] <= 0:
        min_mana_spent = total_mana_spent
        continue

    # Check for loss condition
    if state['player_hp'] <= 0:
        continue

    # Apply effects at the start of the turn
    effects_result = apply_effects(state, state['effects'])
    boss_hp = effects_result['boss_hp']
    mana = effects_result['mana']
    armor = effects_result['armor']
    player_hp = effects_result['player_hp']
    effects = effects_result['effects']

    # Check if boss is dead after effects
    if boss_hp <= 0:
        min_mana_spent = total_mana_spent
        continue

    if state['player_turn']:
        # Player's turn
        # Generate possible moves
        for spell_name, spell in SPELLS.items():
            # Can't cast a spell if we don't have enough mana
            if spell['cost'] > mana:
                continue
            # Can't cast a spell if its effect is already active
            if spell['effect'] and spell['effect']['name'] in effects:
                continue

            # Create new state
            new_state = {
                'player_hp': player_hp,
                'mana': mana - spell['cost'],
                'boss_hp': boss_hp,
                'effects': effects.copy(),
                'armor': 0,
                'mana_spent': total_mana_spent + spell['cost'],
                'player_turn': False  # Next turn is boss's turn
            }

            # Apply the spell immediately if it has instant effects
            new_state['boss_hp'] -= spell['damage']
            new_state['player_hp'] += spell['heal']

            # If the spell starts an effect, add it
            if spell['effect']:
                new_state['effects'][spell['effect']['name']] = spell['effect']['turns']

            # Add the new state to the heap
            heapq.heappush(heap, StateWrapper(new_state['mana_spent'], new_state))
    else:
        # Boss's turn
        # Boss attacks
        damage = max(BOSS_DAMAGE - armor, 1)
        new_state = {
            'player_hp': player_hp - damage,
            'mana': mana,
            'boss_hp': boss_hp,
            'effects': effects.copy(),
            'armor': 0,
            'mana_spent': total_mana_spent,
            'player_turn': True  # Next turn is player's turn
        }
        # Add the new state to the heap
        heapq.heappush(heap, StateWrapper(total_mana_spent, new_state))

# Output the least amount of mana spent
print("Least amount of mana spent to win:", min_mana_spent)
