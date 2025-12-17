# nt_echo_svc API Documentation

Overview

This service provides a simple echo endpoint that accepts a JSON payload with a single field `message` (max 8 characters) and returns the message as plain text.

Error Handling

The API returns HTTP 400 Bad Request for request validation and JSON parsing errors. Error responses use Content-Type: text/plain and contain a short plain-text message describing the problem.

This applies to:
- Request validation errors for the `message` field (missing, empty, or too long)
- Malformed JSON payloads (JSON parsing errors)

HTTP status and Content-Type

- Status: 400 Bad Request
- Content-Type: text/plain

Exact error messages

The API returns the following exact plain-text messages for the corresponding error conditions:

- Error: Message is required
- Error: Message must be 8 characters or fewer
- Error: Invalid request format

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

The wording above matches the service's custom exception handlers and unit tests. Keep these messages unchanged to preserve backward compatibility for clients.
