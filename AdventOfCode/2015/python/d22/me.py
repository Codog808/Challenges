import heapq
from utils import StateWrapper

BOSS_HIT_POINTS = 58
BOSS_DAMAGE = 9

PLAYER_HIT_POINTS = 50
PLAYER_MANA = 500

SPELLS = {
    "Magic Missile":    {
        "cost": 53, 
        "damage": 4, 
        "heal": 0, 
        "effect": None
    },

    "Drain":            {
        "cost": 73, 
        "damage": 2, 
        "heal": 2, 
        "effect": None
    },

    "Shield":           {
        "cost": 113, 
        "damage": 0, 
        "heal": 0, 
        "effect": {
            "name": "Shield", 
            "turns": 6, 
            "armor": 7, 
            "mana": 0, 
            "damage":0}
    },

    "Poison":           {
        "cost": 173, 
        "damage": 0, 
        "heal": 0, 
        "effect": {
            "name": "Poison", 
            "turns": 6, 
            "armor": 0, 
            "mana": 0, 
            "damage": 3}
    },

    "Recharge":         {
        "cost": 229, 
        "damage": 0, 
        "heal": 0, 
        "effect": {
            "name": "Recharge", 
            "turns": 5, 
            "armor": 0, 
            "mana": 101, 
            "damage": 0}
    }
}

initial_state = {
    'effects': {},
    'armor': 0,
    'mana': PLAYER_MANA,
    'boss_hp': BOSS_HIT_POINTS,
    'player_hp': PLAYER_HIT_POINTS,
    'mana_spent': 0,
    'player_turn': True
}

def apply_effects(state, effects):
    new_effects = {}
    armor = 0
    mana = state['mana']
    boss_hp = state['boss_hp']
    player_hp = state['player_hp']

    for effect_name, timer in effects.items():
        if effect_name == "Shield":
            #armor += SPELLS['Shield']['effect']['armor']
            armor += 7
        if effect_name == "Poison":
            #boss_hp -= SPELLS['Poison']['effect']['damage']
            boss_hp -= 3
        if effect_name == "Recharge":
            #mana += SPELLS['Recharge']['effect']['mana']
            mana += 101
        timer -= 1
        if timer > 0:
            new_effects[effect_name] = timer
    
    return {
        "boss_hp": boss_hp,
        "mana": mana,
        "armor": armor,
        "player_hp": player_hp,
        "effects": new_effects
    }



def main():
    visited = {}
    heap = []
    heapq.heappush(heap, StateWrapper(0, initial_state))
    min_mana_spent = float('inf')

    while heap:
        wrapper = heapq.heappop(heap)
        total_mana_spent = wrapper.total_mana_spent
        state = wrapper.state

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

        if total_mana_spent >= min_mana_spent:
            continue
        
        if state['boss_hp'] <= 0:
            min_mana_spent = total_mana_spent
            continue

        if state['player_hp'] <= 0:
            continue

        effects_result = apply_effects(state, state['effects'])
        boss_hp = effects_result['boss_hp']
        mana = effects_result['mana']
        armor = effects_result['armor']
        player_hp = effects_result['player_hp']
        effects = effects_result['effects']

        if boss_hp <= 0:
            min_mana_spent = total_mana_spent
            continue
        
        if state['player_turn']:
            for spell_name, spell in SPELLS.items():
                
                if spell['cost'] > mana:
                    continue

                if spell['effect'] and spell['effect']['name'] in effects:
                    continue

                new_state = {
                    'player_hp': player_hp,
                    'mana': mana - spell['cost'],
                    'boss_hp': boss_hp,
                    'effects': effects.copy(),
                    'armor': 0,
                    'mana_spent': total_mana_spent + spell['cost'],
                    'player_turn': False
                }

                new_state['boss_hp'] -= spell['damage']
                new_state['player_hp'] += spell['heal']

                if spell['effect']:
                    new_state['effects'][spell['effect']['name']] = spell['effect']['turns']

                heapq.heappush(heap, StateWrapper(new_state['mana_spent'], new_state))
        else:
            damage = max(BOSS_DAMAGE - armor, 1)
            new_state = {
                'player_hp': player_hp - damage,
                'mana': mana,
                'boss_hp': boss_hp,
                'effects': effects.copy(),
                'armor': 0,
                'mana_spent': total_mana_spent,
                'player_turn': True
            }
            heapq.heappush(heap, StateWrapper(new_state['mana_spent'], new_state))
    print("Answer to Part 1; Least amount of Mana to Spend:", min_mana_spent)


def main_p2():
    visited = {}
    heap = []
    heapq.heappush(heap, StateWrapper(0, initial_state))
    min_mana_spent = float('inf')

    while heap:
        wrapper = heapq.heappop(heap)
        total_mana_spent = wrapper.total_mana_spent
        state = wrapper.state

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

        if total_mana_spent >= min_mana_spent:
            continue
        
        if state['boss_hp'] <= 0:
            min_mana_spent = total_mana_spent
            continue
    
        state['player_hp'] -= 1
        if state['player_hp'] <= 0:
            continue

        effects_result = apply_effects(state, state['effects'])
        boss_hp = effects_result['boss_hp']
        mana = effects_result['mana']
        armor = effects_result['armor']
        player_hp = effects_result['player_hp']
        effects = effects_result['effects']

        if boss_hp <= 0:
            min_mana_spent = total_mana_spent
            continue
        
        if state['player_turn']:
            for spell_name, spell in SPELLS.items():
                
                if spell['cost'] > mana:
                    continue

                if spell['effect'] and spell['effect']['name'] in effects:
                    continue

                new_state = {
                    'player_hp': player_hp,
                    'mana': mana - spell['cost'],
                    'boss_hp': boss_hp,
                    'effects': effects.copy(),
                    'armor': 0,
                    'mana_spent': total_mana_spent + spell['cost'],
                    'player_turn': False
                }

                new_state['boss_hp'] -= spell['damage']
                new_state['player_hp'] += spell['heal']

                if spell['effect']:
                    new_state['effects'][spell['effect']['name']] = spell['effect']['turns']

                heapq.heappush(heap, StateWrapper(new_state['mana_spent'], new_state))
        else:
            damage = max(BOSS_DAMAGE - armor, 1)
            new_state = {
                'player_hp': player_hp - damage,
                'mana': mana,
                'boss_hp': boss_hp,
                'effects': effects.copy(),
                'armor': 0,
                'mana_spent': total_mana_spent,
                'player_turn': True
            }
            heapq.heappush(heap, StateWrapper(new_state['mana_spent'], new_state))
    print("Answer to Part 2; Least amount of Mana to Spend:", min_mana_spent)

if __name__ == '__main__':
    main()
    main_p2()
