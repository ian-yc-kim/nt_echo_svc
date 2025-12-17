import pathlib


def test_api_md_exists():
    p = pathlib.Path('API.md')
    assert p.exists(), "API.md must exist at project root"


def test_api_md_contains_error_handling():
    text = pathlib.Path('API.md').read_text()
    assert "Error Handling" in text
    # status and content-type
    assert "400" in text and "Bad Request" in text
    assert "text/plain" in text
    # exact required messages
    assert 'Error: Message is required' in text
    assert 'Error: Message must be 8 characters or fewer' in text
    assert 'Error: Invalid request format' in text


def test_api_md_documents_endpoint_and_success():
    text = pathlib.Path('API.md').read_text()
    # endpoint location and method
    assert 'POST /api/echo' in text or ('/api/echo' in text and 'POST' in text)
    # request body contains message field
    assert '"message"' in text or 'message' in text
    # success status and content-type documented
    assert '200' in text and 'OK' in text
    assert 'text/plain' in text
