from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings:
    
    #MCP
    mcp_server_url: str = None

    #Anki
    anki_connect_url: str = None
    anki_deck_name: str = None


    #Postgres
    db_host: str = None
    db_port: int = None
    db_name: str = None
    db_user: str = None
    db_password: str = None
    @property
    def database_url(self) -> str:
        return f"postgresql+psycopg2://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    #Logging
    log_level: str = "INFO"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )
        

@lru_cache
def get_settings() -> Settings:
    return Settings() 

settings = get_settings()