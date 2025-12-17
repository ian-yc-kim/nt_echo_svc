import pathlib


def test_readme_exists():
    p = pathlib.Path('README.md')
    assert p.exists(), "README.md must exist at project root"


def test_readme_contains_docs_reference():
    text = pathlib.Path('README.md').read_text()
    assert '/docs' in text or 'Swagger UI' in text


def test_readme_contains_curl_and_error_example():
    text = pathlib.Path('README.md').read_text()
    # ensure at least one curl example exists
    assert 'curl' in text
    # ensure it documents the specific error message for too long messages
    assert 'Message must be 8 characters or fewer' in text
