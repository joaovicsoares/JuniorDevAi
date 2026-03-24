from pydantic import BaseModel, ConfigDict, Field


class RepositoryRecordCreate(BaseModel):
    """Payload to create a repository record."""

    repo_name: str = Field(min_length=1, max_length=255)
    docker_name: str = Field(min_length=1, max_length=255)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "repo_name": "openai-python",
                    "docker_name": "openai-python-api",
                }
            ]
        }
    }


class RepositoryRecordResponse(BaseModel):
    """Serialized repository record."""

    id: int
    repo_name: str
    docker_name: str

    model_config = ConfigDict(from_attributes=True)
