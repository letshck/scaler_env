import asyncio
import os

from my_env import SmartEnv, SmartAction


BASE_URL = os.getenv("OPENENV_BASE_URL", "http://localhost:8011")


async def run_async_agent():
    print(" Starting Async Agent...\n")
    async with SmartEnv(base_url=BASE_URL) as env:
        result = await env.reset()
        done = False
        step = 0
        while not done:
            obs = result.observation
            print(f"Step {step}")
            print(f"Current: {obs.current_number}, Target: {obs.target}")    
            if obs.current_number < obs.target:
                move = 1
            else:
                move = -1
            print(f"Action Taken: {move}")
            result = await env.step(SmartAction(move=move))
            print(f"Reward: {result.reward}")
            print("-" * 30)
            done = result.done
            step += 1
        print("\n Task Finished!")
if __name__ == "__main__":
    asyncio.run(run_async_agent())