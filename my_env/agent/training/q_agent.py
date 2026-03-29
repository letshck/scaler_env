import pickle
import random
class QLearningAgent:
    def __init__(self):
        self.q_table = {}
        self.actions = [-2, -1, 1, 2]
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.2
    def get_state(self, current, target):
        return (current, target)
    def choose_action(self, current, target):
        state = self.get_state(current, target)
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        self.q_table.setdefault(state, {a: 0 for a in self.actions})
        return max(self.q_table[state], key=self.q_table[state].get)
    def update(self, current, target, action, reward, next_current):
        state = self.get_state(current, target)
        next_state = self.get_state(next_current, target)
        self.q_table.setdefault(state, {a: 0 for a in self.actions})
        self.q_table.setdefault(next_state, {a: 0 for a in self.actions})
        max_future = max(self.q_table[next_state].values())
        old_q = self.q_table[state][action]
        self.q_table[state][action] = old_q + self.alpha * (
            reward + self.gamma * max_future - old_q
        )
    def save(self, path):
        with open(path, "wb") as f:
            pickle.dump(self.q_table, f)
    def load(self, path):
        with open(path, "rb") as f:
            self.q_table = pickle.load(f)