from huggingface_hub import InferenceClient


class SimpleLLMAgent:
    def __init__(self):
        self.client = InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.1")

    def get_action(self, current, target):
        prompt = f"""
Current: {current}
Target: {target}
Choose from [-2,-1,1,2]
Only number:
"""
        try:
            return int(self.client.text_generation(prompt, max_new_tokens=5).strip())
        except Exception:
            return 1
from huggingface_hub import InferenceClient
class SimpleLLMAgent:
    def __init__(self):
        self.client = InferenceClient(
            model="mistralai/Mistral-7B-Instruct-v0.1"
        )
    def get_action(self, current, target):
        prompt = f"""
Current: {current}
Target: {target}
Choose from [-2,-1,1,2]
Only number:
"""
        try:
            return int(self.client.text_generation(prompt, max_new_tokens=5).strip())
        except:
            return 1