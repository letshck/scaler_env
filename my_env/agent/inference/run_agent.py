import os

from my_env import SmartEnv, SmartAction
from my_env.agent.inference.policy_agent import PolicyAgent
from my_env.agent.inference.llm_agent import SimpleLLMAgent

BASE_URL = os.getenv("OPENENV_BASE_URL", "http://localhost:8011")

policy = PolicyAgent("my_env/agent/saved_models/q_table.pkl")
llm = SimpleLLMAgent()

with SmartEnv(base_url=BASE_URL).sync() as env:
    result = env.reset()
    done = False
    while not done:
        obs = result.observation
        action = policy.get_action(obs.current_number, obs.target)
        if action is None:
            action = llm.get_action(obs.current_number, obs.target)
        result = env.step(SmartAction(move=action))
        done = result.done
print("Finished!")