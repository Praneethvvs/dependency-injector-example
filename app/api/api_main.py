import uvicorn

from app.api.api_bootstrap import ServiceBootStrap

print("starting up application....")
service_api = ServiceBootStrap.create_service_api()


# add any life span events if required in this file
