from fastapi import FastAPI
from openenv.core.env_server import create_app
from .environment import SmartEnvironment
from ..models import SmartAction, SmartObservation
def _env_factory() -> SmartEnvironment:
	return SmartEnvironment()
app: FastAPI = create_app(_env_factory, SmartAction, SmartObservation)