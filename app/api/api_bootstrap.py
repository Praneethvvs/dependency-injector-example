from fastapi import FastAPI

from app.api import endpoints
from app.init.di_container import ServiceDIContainer


class ServiceBootStrap:
    API_ROUTE_PREFIX: str = "/api"

    @staticmethod
    def create_service_api() -> FastAPI:
        container = ServiceDIContainer()
        container.init_resources()
        # wiring the container with endpoints module
        container.wire(modules=[endpoints])
        # starting up application
        service_api: FastAPI = FastAPI()
        service_api.include_router(
            endpoints.router,
            prefix=ServiceBootStrap.API_ROUTE_PREFIX,
        )
        return service_api

    @staticmethod
    def post_api_service_setup():
        # add middleware here if required and call this method in create_service_api()
        pass
