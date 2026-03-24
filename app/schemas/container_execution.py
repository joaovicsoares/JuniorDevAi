from pydantic import BaseModel


class ContainerExecutionResponse(BaseModel):
    """Result of resolving a repository to a container and running a command."""

    repo_name: str
    docker_name: str
    container_running: bool
    command: list[str]
    output: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "repo_name": "openai-python",
                    "docker_name": "openai-python-api",
                    "container_running": True,
                    "command": ["echo", "hello world"],
                    "output": "hello world",
                }
            ]
        }
    }
