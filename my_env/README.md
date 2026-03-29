# Smart Target Environment
A simple reinforcement learning environment where an agent learns to reach a target number.

## How it works
- Agent starts at 0
- Target is random
- Agent can add/subtract numbers
- Reward:
  - Closer → better
  - Exact match → BIG reward

## Run locally
From `D:/cyber_rl_env`:

```powershell
.\.venv\Scripts\Activate.ps1
d:/cyber_rl_env/.venv/Scripts/python.exe -m uvicorn my_env.server.app:app --host 127.0.0.1 --port 8010
```

In a second terminal (quick smoke test):

```powershell
d:/cyber_rl_env/.venv/Scripts/python.exe -c "from my_env import SmartEnv, SmartAction; s = SmartEnv(base_url='http://127.0.0.1:8010').sync(); s.__enter__(); r = s.reset(); t = s.step(SmartAction(move=1)); print('target=', r.observation.target, 'reward=', t.reward, 'done=', t.done); s.__exit__(None, None, None)"
```

## Deploy with Docker
Build from `D:/cyber_rl_env`:

```powershell
docker build -f my_env/server/Dockerfile -t smart-target-env:latest .
```

Run container:

```powershell
docker run --rm -p 8011:8000 --name smart-target-env smart-target-env:latest
```

If port `8011` is already in use, you can map to `8000` instead:

```powershell
docker run --rm -p 8000:8000 --name smart-target-env smart-target-env:latest
```

Health check:

```powershell
Invoke-WebRequest http://127.0.0.1:8011/docs
```

## Example
```python
from smart_target_env import SmartEnv, SmartAction
with SmartEnv(base_url="YOUR_HF_SPACE").sync() as env:
    env.reset()
    result = env.step(SmartAction(move=2))
    print(result)