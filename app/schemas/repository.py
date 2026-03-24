from pydantic import BaseModel, HttpUrl


class RepositoryLinkRequest(BaseModel):
    """Request payload containing a GitHub repository URL."""

    repo_url: HttpUrl

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "repo_url": "https://github.com/openai/openai-python",
                }
            ]
        }
    }


class RepositoryLinkResponse(BaseModel):
    """Normalized GitHub repository data extracted from a URL."""

    provider: str
    owner: str
    repository: str
    repo_url: HttpUrl
    clone_url: HttpUrl
    api_url: HttpUrl

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "provider": "github",
                    "owner": "openai",
                    "repository": "openai-python",
                    "repo_url": "https://github.com/openai/openai-python",
                    "clone_url": "https://github.com/openai/openai-python.git",
                    "api_url": "https://api.github.com/repos/openai/openai-python",
                }
            ]
        }
    }
