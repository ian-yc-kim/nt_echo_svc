from fastapi import FastAPI

"""Application factory for nt_echo_svc.

This module exposes the FastAPI app instance. The root_path parameter
was previously set to an undefined name which caused import-time
NameError in tests. Use default FastAPI initialization here and
mount routers elsewhere to avoid side effects at import time.
"""

app = FastAPI(debug=True)

# add routers
