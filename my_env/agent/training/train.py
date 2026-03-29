import os
from my_env import SmartEnv, SmartAction
from my_env.agent.training.q_agent import QLearningAgent
BASE_URL = os.getenv("OPENENV_BASE_URL", "http://localhost:8011")
agent = QLearningAgent()
with SmartEnv(base_url=BASE_URL).sync() as env:
    for episode in range(100):
        result = env.reset()
        done = False
        while not done:
            obs = result.observation

            action = agent.choose_action(
                obs.current_number,
                obs.target
            )
            result = env.step(SmartAction(move=action))

            agent.update(
                obs.current_number,
                obs.target,
                action,
                result.reward,
                result.observation.current_number
            )
            done = result.done
agent.save("my_env/agent/saved_models/q_table.pkl")
print("Training Done!")