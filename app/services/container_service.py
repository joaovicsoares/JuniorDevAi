import docker
from docker.errors import DockerException, NotFound

from app.core.exceptions import BadRequestException, NotFoundException
from app.schemas.container_execution import ContainerExecutionResponse


class ContainerService:
    """Operations for inspecting and executing commands in Docker containers."""

    def execute_hello_world(
        self,
        repo_name: str,
        docker_name: str,
    ) -> ContainerExecutionResponse:
        command = ["echo", "hello world"]

        try:
            client = docker.from_env()
            container = client.containers.get(docker_name)
        except NotFound as exc:
            raise NotFoundException(
                f"Container '{docker_name}' was not found."
            ) from exc
        except DockerException as exc:
            raise BadRequestException(
                "Could not connect to Docker from the API container."
            ) from exc

        container.reload()
        if container.status != "running":
            raise BadRequestException(f"Container '{docker_name}' is not running.")

        try:
            exit_code, output = container.exec_run(command)
        except DockerException as exc:
            raise BadRequestException(
                f"Failed to execute command in container '{docker_name}'."
            ) from exc

        decoded_output = output.decode("utf-8", errors="replace").strip()
        if exit_code != 0:
            raise BadRequestException(
                f"Command failed in container '{docker_name}' with exit code {exit_code}."
            )

        return ContainerExecutionResponse(
            repo_name=repo_name,
            docker_name=docker_name,
            container_running=True,
            command=command,
            output=decoded_output,
        )
