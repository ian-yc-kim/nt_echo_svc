from pydantic import BaseModel, Field


class EchoRequest(BaseModel):
    """Pydantic model for echo requests.

    Fields
    - message: required string with length between 1 and 8 inclusive.
    """

    message: str = Field(..., min_length=1, max_length=8)
