import traceback

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, FastAPI, HTTPException
from pydantic import BaseModel

from app.init.di_container import ServiceDIContainer
from app.service.logging_service import LogEntry


class UserMessage(BaseModel):
    username: str
    message: str


router = APIRouter()


@router.post("/log_message/")
@inject
async def log_message(
    user_message: UserMessage,
    log_entry_service: LogEntry = Depends(
        Provide[ServiceDIContainer.log_entry_service],
    ),
):
    try:
        log_entry_service.log(user_message.username, user_message.message)
    except Exception as e:
        traceback.print_exc()
        print("Exception Occured", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

    return {"status": "success", "message": "your entry has been logged successfully"}
