# nt_echo_svc

A minimal echo service that accepts a JSON payload containing a short message and returns it as plain text.

Docs

See API.md for full API documentation and exact error messages.

Run locally

Install dependencies and run the service:

poetry install

# Option A: run packaged entrypoint
poetry run nt_echo_svc

# Option B: run via uvicorn
uvicorn nt_echo_svc.app:app --reload --port 8000

Quick curl example

curl -X POST http://127.0.0.1:8000/api/echo \
  -H "Content-Type: application/json" \
  -d '{"message":"hello"}'

Expected response: plain text body containing the echoed message (hello).
