# nt_echo_svc API Documentation

Note: Interactive Swagger UI is available at /docs when the service is running. You can also view the raw OpenAPI schema at /openapi.json.

Overview

This service provides a simple echo endpoint that accepts a JSON payload with a single field `message` (1..8 characters) and returns the message as plain text.

Endpoint

- Method: POST
- Path: /api/echo
- Content-Type: application/json

Request Body

The request body must be a JSON object with a single required property:

{
  "message": string  # length between 1 and 8 characters inclusive
}

Success Response

- Status: 200 OK
- Content-Type: text/plain; charset=utf-8
- Body: The plain text message that was provided in the request

Example Success

Request

POST /api/echo
Content-Type: application/json

{"message": "hello"}

Response

200 OK
Content-Type: text/plain

hello

Error Handling

Validation and JSON parsing errors return HTTP 400 Bad Request and plain-text bodies (Content-Type: text/plain). The service uses custom handlers to produce concise, exact error messages for common cases.

Exact error messages

The API returns the following exact plain-text messages for the corresponding error conditions:

- Error: Message is required
- Error: Message must be 8 characters or fewer
- Error: Invalid request format

Fallback for other validation issues

Other validation errors (for example type mismatches or unexpected validation errors) return:

- Error: Invalid request

Examples

1) Missing message field

Response: 400 Bad Request
Content-Type: text/plain
Body: Error: Message is required

2) Message too long

Response: 400 Bad Request
Content-Type: text/plain
Body: Error: Message must be 8 characters or fewer

3) Malformed JSON

Response: 400 Bad Request
Content-Type: text/plain
Body: Error: Invalid request format

Notes

- Keep the exact error message text as-is to preserve backward compatibility for clients.
- The documented endpoint path is POST /api/echo (router path /echo with app prefix /api).
