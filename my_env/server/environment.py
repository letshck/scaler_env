import random
from typing import Any, Optional

from openenv.core.env_server.interfaces import Environment
from ..models import SmartAction, SmartObservation, SmartState
class SmartEnvironment(Environment):
    def __init__(self):
        self._state = None
    def reset(
        self,
        seed: Optional[int] = None,
        episode_id: Optional[str] = None,
        **kwargs: Any,
    ) -> SmartObservation:
        target = random.randint(5, 20)
        self._state = SmartState(
            step_count=0,
            current_number=0,
            target=target
        )
        return SmartObservation(
            current_number=0,
            target=target,
            message=" Reach the target number",
            reward=0,
            done=False,
        )

    def step(
        self,
        action: SmartAction,
        timeout_s: Optional[float] = None,
        **kwargs: Any,
    ) -> SmartObservation:
        self._state.step_count += 1
        self._state.current_number += action.move
        distance = abs(self._state.target - self._state.current_number)
        reward = -distance * 0.1
        done = False
        message = ""
#for win
        if self._state.current_number == self._state.target:
            reward = 10
            done = True
            message = "Perfect, Target reached!"
        elif self._state.step_count > 20:
            done = True
            message = " Too many steps!"
        else:
            message = f"Distance: {distance}"
        return SmartObservation(
            current_number=self._state.current_number,
            target=self._state.target,
            message=message,
            reward=reward,
            done=done,
        )

    @property
    def state(self) -> SmartState:
        return self._state