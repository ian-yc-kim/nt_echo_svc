import pytest
from pydantic import ValidationError

from nt_echo_svc.schemas import EchoRequest


def test_valid_min_length():
    req = EchoRequest(message="a")
    assert req.message == "a"


def test_valid_max_length():
    s = "12345678"
    req = EchoRequest(message=s)
    assert req.message == s


def test_empty_string_raises():
    with pytest.raises(ValidationError):
        EchoRequest(message="")


def test_too_long_raises():
    with pytest.raises(ValidationError):
        EchoRequest(message="123456789")


def test_missing_field_raises():
    with pytest.raises(ValidationError):
        EchoRequest()
