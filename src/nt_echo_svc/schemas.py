from pydantic import BaseModel, Field, ConfigDict


class EchoRequest(BaseModel):
    """Pydantic model for echo requests.

    Fields
    - message: required string with length between 1 and 8 inclusive.
    """

    # Provide OpenAPI example payload for schema documentation
    model_config = ConfigDict(json_schema_extra={"example": {"message": "hello"}})

    message: str = Field(..., min_length=1, max_length=8)
