import logging
from json import JSONDecodeError
from typing import Any

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse


async def request_validation_handler(request: Request, exc: RequestValidationError) -> PlainTextResponse:
    """Handle request validation errors and return plain text responses.

    This handler inspects validation errors and returns user-friendly
    plain text messages for known cases related to the `message` field.
    """
    try:
        for err in exc.errors():
            err_type = err.get("type", "")
            loc = err.get("loc", ())

            # Determine if this error refers to the `message` field
            is_message_field = False
            try:
                if isinstance(loc, (list, tuple)) and len(loc) > 0:
                    is_message_field = loc[-1] == "message"
            except Exception:
                is_message_field = False

            # Missing or empty message
            if is_message_field and err_type in ("missing", "string_too_short", "too_short", "value_error.missing"):
                return PlainTextResponse("Error: Message is required", status_code=400)

            # Message too long
            if is_message_field and err_type in ("string_too_long", "too_long", "value_error.any_str.max_length"):
                return PlainTextResponse("Error: Message must be 8 characters or fewer", status_code=400)

            # JSON decode-like errors surfaced by validation
            if err_type in ("json_invalid", "value_error.jsondecode"):
                return PlainTextResponse("Error: Invalid request format", status_code=400)

        # Fallback for other validation problems
        return PlainTextResponse("Error: Invalid request", status_code=400)
    except Exception as e:
        logging.error(e, exc_info=True)
        return PlainTextResponse("Error: Invalid request", status_code=400)


async def json_decode_handler(request: Request, exc: JSONDecodeError) -> PlainTextResponse:
    """Handle raw JSON decoding errors and return a plain text response."""
    try:
        return PlainTextResponse("Error: Invalid request format", status_code=400)
    except Exception as e:
        logging.error(e, exc_info=True)
        return PlainTextResponse("Error: Invalid request format", status_code=400)
