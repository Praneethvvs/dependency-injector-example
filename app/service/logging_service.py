import datetime

from app.configuration.config_model import AppConfig


class LogEntry:
    def __init__(self, app_config: AppConfig):
        print("returning new instance for LogEntry")
        self.timestamp = datetime.datetime.now()
        self.app_config = app_config

    def log(self, username, message):
        # Simulate logging by printing to console
        print(
            {
                "app_version": f"{self.app_config.LogConfig.app_version}",
                "username": f"{username}",
                "message": f"{self.app_config.LogConfig.log_prefix}:{self.timestamp}: {message}",
            }
        )
