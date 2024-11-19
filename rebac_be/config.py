from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Rebac Backend"
    permit_api_url: str
    permit_proj_id: str
    permit_env: str
    permit_api_key: str

    model_config = SettingsConfigDict(env_file=".env")
    

settings = Settings()
