import os

from my_env import SmartAction, SmartEnv


def choose_action(current: int, target: int) -> int:
    if current < target:
        return 1
    if current > target:
        return -1
    return 0


def main() -> None:
    base_url = os.getenv("OPENENV_BASE_URL", "http://127.0.0.1:8011")

    with SmartEnv(base_url=base_url).sync() as env:
        result = env.reset()
        done = result.done

        while not done:
            obs = result.observation
            action = choose_action(obs.current_number, obs.target)
            result = env.step(SmartAction(move=action))
            done = result.done

    print("inference completed")


if __name__ == "__main__":
    main()
