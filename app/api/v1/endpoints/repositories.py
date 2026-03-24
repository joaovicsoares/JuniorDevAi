from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, status

from app.api.deps import get_db
from app.schemas.container_execution import ContainerExecutionResponse
from app.schemas.repository import RepositoryLinkRequest, RepositoryLinkResponse
from app.schemas.repository_record import (
    RepositoryRecordCreate,
    RepositoryRecordResponse,
)
from app.services.container_service import ContainerService
from app.services.repository_record_service import RepositoryRecordService
from app.services.repository_service import RepositoryService

router = APIRouter()


def get_repository_service() -> RepositoryService:
    """Dependency injector for RepositoryService."""
    return RepositoryService()


def get_repository_record_service(
    session: AsyncSession = Depends(get_db),
) -> RepositoryRecordService:
    """Dependency injector for RepositoryRecordService."""
    return RepositoryRecordService(session)


def get_container_service() -> ContainerService:
    """Dependency injector for ContainerService."""
    return ContainerService()


@router.post(
    "/parse",
    response_model=RepositoryLinkResponse,
    status_code=status.HTTP_200_OK,
    summary="Parse a GitHub repository link",
    description="Validates a GitHub repository URL and returns normalized repository data.",
)
async def parse_repository_link(
    payload: RepositoryLinkRequest,
    service: RepositoryService = Depends(get_repository_service),
) -> RepositoryLinkResponse:
    return service.parse_github_repo_url(str(payload.repo_url))


@router.post(
    "/execute",
    response_model=ContainerExecutionResponse,
    status_code=status.HTTP_200_OK,
    summary="Execute a command in the mapped repository container",
    description=(
        "Parses the GitHub repository URL, finds the matching repository in the "
        "database, verifies the mapped container is running, and executes a demo command."
    ),
)
async def execute_repository_container_command(
    payload: RepositoryLinkRequest,
    repository_service: RepositoryService = Depends(get_repository_service),
    record_service: RepositoryRecordService = Depends(get_repository_record_service),
    container_service: ContainerService = Depends(get_container_service),
) -> ContainerExecutionResponse:
    parsed_repository = repository_service.parse_github_repo_url(str(payload.repo_url))
    record = await record_service.get_by_repo_name(parsed_repository.repository)
    return container_service.execute_hello_world(
        repo_name=record.repo_name,
        docker_name=record.docker_name,
    )


@router.post(
    "/",
    response_model=RepositoryRecordResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a repository record",
    description="Stores a repository name and docker image/container name in the database.",
)
async def create_repository_record(
    payload: RepositoryRecordCreate,
    service: RepositoryRecordService = Depends(get_repository_record_service),
) -> RepositoryRecordResponse:
    return await service.create(payload)


@router.get(
    "/",
    response_model=list[RepositoryRecordResponse],
    status_code=status.HTTP_200_OK,
    summary="List repository records",
    description="Returns all repository records stored in the database.",
)
async def list_repository_records(
    service: RepositoryRecordService = Depends(get_repository_record_service),
) -> list[RepositoryRecordResponse]:
    return await service.list_all()
