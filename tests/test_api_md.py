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
