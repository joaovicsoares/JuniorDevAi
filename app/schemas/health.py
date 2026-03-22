from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Schema returned by the health-check endpoint."""

    status: str
    version: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": "healthy",
                    "version": "0.1.0",
                }
            ]
        }
    }
