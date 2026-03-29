from openenv.core.env_client import EnvClient
from openenv.core.client_types import StepResult
from .models import SmartAction, SmartObservation, SmartState
class SmartEnv(EnvClient[SmartAction, SmartObservation, SmartState]):
    def _step_payload(self, action: SmartAction) -> dict:
        return action.model_dump()
    def _parse_result(self, payload: dict) -> StepResult[SmartObservation]:
        observation_data = payload.get("observation", {})
        observation = SmartObservation(
            **observation_data,
            reward=payload.get("reward"),
            done=payload.get("done", False),
        )
        return StepResult(
            observation=observation,
            reward=payload.get("reward"),
            done=payload.get("done", False),
        )

    def _parse_state(self, payload: dict) -> SmartState:
        return SmartState(**payload)