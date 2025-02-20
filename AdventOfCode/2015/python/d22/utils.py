class StateWrapper:
    def __init__(self, total_mana_spent, state):
        self.total_mana_spent = total_mana_spent
        self.state = state

    def __lt__(self, other):
        return self.total_mana_spent < other.total_mana_spent


