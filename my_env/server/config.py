ATTACK_ACTIONS = {
    0: "Scan",
    1: "Brute Force",
    2: "SQL Injection",
    3: "Exploit"
}
DEFENSE_ACTIONS = {
    0: "Monitor",
    1: "Block IP",
    2: "Patch System",
    3: "Close Port"
}
ATTACK_SUCCESS = 10
DEFENSE_SUCCESS = -10
DETECTION = -5
STEP_PENALTY = -1
MAX_STEPS = 10