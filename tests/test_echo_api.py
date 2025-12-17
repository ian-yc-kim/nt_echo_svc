def test_success_basic(client):
    resp = client.post('/api/echo', json={'message': 'hello'})
    assert resp.status_code == 200
    assert resp.text == 'hello'
    assert resp.headers.get('content-type', '').startswith('text/plain')


def test_success_boundary(client):
    resp = client.post('/api/echo', json={'message': '12345678'})
    assert resp.status_code == 200
    assert resp.text == '12345678'
    assert resp.headers.get('content-type', '').startswith('text/plain')


def test_error_missing_field(client):
    resp = client.post('/api/echo', json={})
    assert resp.status_code == 400
    assert resp.text == 'Error: Message is required'
    assert resp.headers.get('content-type', '').startswith('text/plain')


def test_error_empty_string(client):
    resp = client.post('/api/echo', json={'message': ''})
    assert resp.status_code == 400
    assert resp.text == 'Error: Message is required'
    assert resp.headers.get('content-type', '').startswith('text/plain')


def test_error_too_long(client):
    resp = client.post('/api/echo', json={'message': '123456789'})
    assert resp.status_code == 400
    assert resp.text == 'Error: Message must be 8 characters or fewer'
    assert resp.headers.get('content-type', '').startswith('text/plain')


def test_error_malformed_json(client):
    # send deliberately malformed JSON bytes with content-type header
    resp = client.post('/api/echo', content=b'{"bad":', headers={'Content-Type': 'application/json'})
    assert resp.status_code == 400
    assert resp.text == 'Error: Invalid request format'
    assert resp.headers.get('content-type', '').startswith('text/plain')
