from typing import Type, Tuple, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict, PydanticBaseSettingsSource
from functools import lru_cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    
    #MCP
    mcp_server_url: Optional[str] = None

    #Anki
    anki_connect_url: Optional[str] = None
    anki_deck_name: Optional[str] = None

    #LLM
    model: Optional[str] = None
    model_provider: Optional[str] = None
    api_version: Optional[str] = None
    endpoint: Optional[str] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None

    #Postgres
    db_host: Optional[str] = None
    db_port: Optional[int] = None
    db_name: Optional[str] = None
    db_user: Optional[str] = None
    db_password: Optional[str] = None
    @property
    def database_url(self) -> Optional[str]:
        return f"postgresql+psycopg2://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    #Logging
    log_level: Optional[str] = "INFO"
    
    @classmethod
    def settings_customise_source(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        #Priority : Init args > Env vars > .env file > others(e.g. Azure Keyvault if implemented)
        return init_settings, env_settings, dotenv_settings
    
        

# @lru_cache
# def get_settings() -> Settings:
#     return Settings() 

settings = Settings()

if __name__ == "__main__":
    print(settings.model)