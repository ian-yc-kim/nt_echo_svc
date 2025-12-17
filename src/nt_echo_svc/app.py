from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from json import JSONDecodeError

"""Application factory for nt_echo_svc.

This module exposes the FastAPI app instance. The root_path parameter
was previously set to an undefined name which caused import-time
NameError in tests. Use default FastAPI initialization here and
mount routers elsewhere to avoid side effects at import time.
"""

app = FastAPI(debug=True)

# Register custom exception handlers
from .handlers import request_validation_handler, json_decode_handler
app.add_exception_handler(RequestValidationError, request_validation_handler)
app.add_exception_handler(JSONDecodeError, json_decode_handler)

# add routers
from nt_echo_svc.routers import echo_router
app.include_router(echo_router, prefix="/api")
