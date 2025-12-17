from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
import logging

from nt_echo_svc.schemas import EchoRequest

echo_router = APIRouter()

@echo_router.post("/echo", response_class=PlainTextResponse)
async def echo(request: EchoRequest) -> PlainTextResponse:
    """Echo endpoint returns the request.message as plain text.

    Pydantic validation runs before this handler, global handlers
    handle validation and JSON decode errors.
    """
    try:
        return PlainTextResponse(request.message)
    except Exception as e:
        logging.error(e, exc_info=True)
        return PlainTextResponse("Error: Invalid request", status_code=400)
