import logging

from dependency_injector import containers, providers

from app.configuration.config_parser import ConfigParser
from app.service.logging_service import LogEntry


class ServiceDIContainer(containers.DeclarativeContainer):

    # Use providers.Singleton as the app_config needs to return the same instance everytime
    app_config = providers.Singleton(
        ConfigParser.load_config,
        file_path="app/configuration/config.yml",
    )

    # Use providers.Factory as the logger needs to create a new instance everytime
    log_entry_service = providers.Factory(
        LogEntry,
        app_config,
    )
