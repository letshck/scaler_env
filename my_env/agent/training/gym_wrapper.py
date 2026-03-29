"""
Central configuration file for agents
Keep all important constants here
"""
BASE_URL = "http://localhost:8000"
EPISODES = 100
MAX_STEPS = 20

#RL Agent Parameters
ACTIONS = [-2, -1, 1, 2]
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.9
EPSILON = 0.2
#Model Paths
MODEL_PATH = "agent/saved_models/q_table.pkl"

HF_MODEL = "mistralai/Mistral-7B-Instruct-v0.1"
MAX_TOKENS = 10

DEBUG = True
LOG_EVERY_STEP = True