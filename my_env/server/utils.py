import random
def simulate_attack(state, action):
    weak_pass = state[2]
    sql_vuln = state[3]
    if action == 1 and weak_pass:
        return True
    if action == 2 and sql_vuln:
        return True
    if action == 3:
        return True
    return False
def simulate_defense(state, action):
    blocked = False
    detected = False
    if action == 1:
        blocked = True
    elif action == 2:
        state[2] = 0
        state[3] = 0
    elif action == 3:
        state[0] = 0
        state[1] = 0
    return state, blocked, detected
def calculate_reward(attack_success, blocked):
    if attack_success and not blocked:
        return 12,"Hacker Wins!"

    elif blocked:
        return -12,"Defender Wins!"

    else:
        return -1,"No one wins..."