# nt_echo_svc

A minimal echo service that accepts a JSON payload containing a short message and returns it as plain text.

Docs

See API.md for full API documentation and exact error messages.

Swagger UI / OpenAPI

An interactive Swagger UI is available when the service is running at http://127.0.0.1:8000/docs
You can also fetch the raw OpenAPI schema at http://127.0.0.1:8000/openapi.json

Run locally

Install dependencies and run the service:

poetry install

# Option A: run packaged entrypoint
poetry run nt_echo_svc

# Option B: run via uvicorn
uvicorn nt_echo_svc.app:app --reload --port 8000

Quick curl examples

Success example

curl -X POST http://127.0.0.1:8000/api/echo \
  -H "Content-Type: application/json" \
  -d '{"message":"hello"}'

Expected response: 200 OK with a plain text body containing the echoed message (hello).
Response Content-Type: text/plain

Error example (message too long)

# This message is 9 characters long, exceeding the 8 char limit
curl -X POST http://127.0.0.1:8000/api/echo \
  -H "Content-Type: application/json" \
  -d '{"message":"123456789"}'

Expected response: 400 Bad Request with plain text body:
Error: Message must be 8 characters or fewer
Response Content-Type: text/plain

Error example (malformed JSON)

curl -X POST http://127.0.0.1:8000/api/echo \
  -H "Content-Type: application/json" \
  --data-binary '{"bad":'

Expected response: 400 Bad Request with plain text body:
Error: Invalid request format

Notes

- Responses (both success and error) are returned as text/plain, not JSON.
- Interactive API documentation is available at /docs for quick testing and exploration.
