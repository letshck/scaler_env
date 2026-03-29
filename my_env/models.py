from pydantic import BaseModel
from openenv.core.env_server.interfaces import Action, Observation, State
class SmartAction(Action):
    move: int
class SmartObservation(Observation):
    current_number: int
    target: int
    message: str
class SmartState(State):
    step_count: int
    current_number: int
    target: int
class StepResult(BaseModel):
    observation: SmartObservation
    reward: float
    done: bool