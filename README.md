# Smart Target RL Environment

This repository contains a reinforcement learning environment and agent toolkit under [my_env](my_env/README.md).

## Quick Start

1. Create and activate your virtual environment.
2. Install dependencies from [my_env/pyproject.toml](my_env/pyproject.toml) and [my_env/server/requirements.txt](my_env/server/requirements.txt).
3. Follow run instructions in [my_env/README.md](my_env/README.md).

## Main Components

- `my_env/server`: FastAPI environment server
- `my_env/agent/training`: Training utilities and Q-learning agent
- `my_env/agent/inference`: Inference-time agent runners
- `my_env/client.py`: Client integration helpers

For full usage and examples, see [my_env/README.md](my_env/README.md).
