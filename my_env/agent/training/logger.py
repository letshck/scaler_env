import os
LOG_FILE = "outputs/logs/training_log.txt"
def log(message):
    os.makedirs("outputs/logs", exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")