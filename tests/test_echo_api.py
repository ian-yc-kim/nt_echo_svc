def test_echo_success(client):
    resp = client.post('/api/echo', json={'message': 'hello'})
    assert resp.status_code == 200
    assert resp.text == 'hello'
    assert resp.headers.get('content-type', '').startswith('text/plain')


def test_echo_boundary_max_length(client):
    resp = client.post('/api/echo', json={'message': '12345678'})
    assert resp.status_code == 200
    assert resp.text == '12345678'


def test_echo_validation_and_error_handlers(client):
    # empty message
    resp = client.post('/api/echo', json={'message': ''})
    assert resp.status_code == 400
    assert resp.text == 'Error: Message is required'
    assert resp.headers.get('content-type', '').startswith('text/plain')

    # too long message
    resp = client.post('/api/echo', json={'message': '123456789'})
    assert resp.status_code == 400
    assert resp.text == 'Error: Message must be 8 characters or fewer'
    assert resp.headers.get('content-type', '').startswith('text/plain')

    # malformed JSON
    resp = client.post('/api/echo', content=b'{"mess"', headers={'Content-Type': 'application/json'})
    assert resp.status_code == 400
    assert resp.text == 'Error: Invalid request format'
    assert resp.headers.get('content-type', '').startswith('text/plain')
