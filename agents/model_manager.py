from backend.app.config.settings import settings
from langchain.chat_models import init_chat_model, BaseChatModel

class ModelManager:

    def __init__(self):
        
        self.model = settings.model
        self.model_provider = settings.model_provider
        self.api_version = settings.api_version
        self.endpoint = settings.endpoint
        self.temperature = settings.temperature
        self.max_tokens = settings.mac_tokens

    def select_model(self) -> BaseChatModel:

        return init_chat_model(model=f"{self.model_provider}:{self.model}",temperature=self.temperature)
