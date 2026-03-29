import pickle
class PolicyAgent:
    def __init__(self, path):
        with open(path, "rb") as f:
            self.q_table = pickle.load(f)
    def get_action(self, current, target):
        state = (current, target)
        if state not in self.q_table:
            return None
        return max(self.q_table[state], key=self.q_table[state].get)