import os

import yaml
from pydantic import ValidationError

from app.configuration.config_model import AppConfig


class ConfigParser:
    @staticmethod
    def load_config(file_path: str):
        with open(file_path, "r") as yaml_file:
            yaml_content = yaml.safe_load(yaml_file)
        app_config = ConfigParser.validate_configuration(yaml_content)
        print("Loaded Config")
        return app_config

    def validate_configuration(config):
        try:
            print("validating config....")
            return AppConfig(**config)
        except ValidationError as e:
            raise Exception(f"Configuration validation error: {e}")
