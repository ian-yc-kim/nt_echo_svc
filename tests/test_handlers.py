import pytest
from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

from nt_echo_svc.app import app
from nt_echo_svc.schemas import EchoRequest


@pytest.fixture(autouse=True)
def test_echo_route():
    """Register a temporary test router before TestClient is created.

    This autouse fixture ensures the test-only route is present when
    the shared TestClient fixture from conftest.py constructs the client.
    It also removes the test route after tests in this module finish.
    """
    router = APIRouter()

    @router.post('/__test__/echo')
    async def __test_echo(payload: EchoRequest):
        return PlainTextResponse(payload.message)

    app.include_router(router)
    yield

    # Teardown: remove any routes that were registered for the test prefix
    try:
        app.router.routes = [r for r in app.router.routes if not getattr(r, 'path', '').startswith('/__test__/echo')]
    except Exception:
        # best-effort cleanup; do not fail tests on teardown
        pass


def test_missing_field_returns_400_and_message(client):
    resp = client.post('/__test__/echo', json={})
    assert resp.status_code == 400
    assert resp.text == 'Error: Message is required'
    assert resp.headers.get('content-type', '').startswith('text/plain')


def test_empty_string_returns_400_and_message(client):
    resp = client.post('/__test__/echo', json={'message': ''})
    assert resp.status_code == 400
    assert resp.text == 'Error: Message is required'
    assert resp.headers.get('content-type', '').startswith('text/plain')


def test_too_long_message_returns_400_and_message(client):
    resp = client.post('/__test__/echo', json={'message': '123456789'})
    assert resp.status_code == 400
    assert resp.text == 'Error: Message must be 8 characters or fewer'
    assert resp.headers.get('content-type', '').startswith('text/plain')


def test_malformed_json_returns_400_and_format_error(client):
    # send malformed JSON bytes with proper content-type
    resp = client.post('/__test__/echo', content=b'{"mess"', headers={'Content-Type': 'application/json'})
    assert resp.status_code == 400
    assert resp.text == 'Error: Invalid request format'
    assert resp.headers.get('content-type', '').startswith('text/plain')
