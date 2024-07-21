from pydantic import BaseModel


class LogConfig(BaseModel):
    app_version: str
    log_prefix: str


class AppConfig(BaseModel):
    LogConfig: LogConfig
