from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
import logging

from nt_echo_svc.schemas import EchoRequest

echo_router = APIRouter()

@echo_router.post(
    "/echo",
    response_class=PlainTextResponse,
    summary="Echo a message",
    description=(
        "Accepts a JSON payload with a single field `message` (1-8 characters). "
        "Returns the message as a text/plain response. Validation and JSON decode "
        "errors return 400 with plain text error messages."
    ),
    responses={
        200: {
            "description": "Successful echo",
            "content": {"text/plain": {"example": "hello"}},
        },
        400: {
            "description": "Invalid input",
            "content": {
                "text/plain": {
                    "examples": {
                        "missing": {
                            "summary": "Missing message",
                            "value": "Error: Message is required",
                        },
                        "too_long": {
                            "summary": "Message too long",
                            "value": "Error: Message must be 8 characters or fewer",
                        },
                        "invalid_format": {
                            "summary": "Invalid JSON format",
                            "value": "Error: Invalid request format",
                        },
                    }
                }
            },
        },
    },
)
async def echo(request: EchoRequest) -> PlainTextResponse:
    """Echo endpoint returns the request.message as plain text.

    Request:
    - JSON object with `message` string between 1 and 8 characters.

    Responses:
    - 200 text/plain: the echoed message (example: "hello").
    - 400 text/plain: validation or format errors. Examples include:
        - Error: Message is required
        - Error: Message must be 8 characters or fewer
        - Error: Invalid request format
    """
    try:
        return PlainTextResponse(request.message)
    except Exception as e:
        logging.error(e, exc_info=True)
        return PlainTextResponse("Error: Invalid request", status_code=400)
