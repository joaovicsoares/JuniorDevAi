from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.repository_record import RepositoryRecord
from app.core.exceptions import NotFoundException
from app.schemas.repository_record import (
    RepositoryRecordCreate,
    RepositoryRecordResponse,
)


class RepositoryRecordService:
    """Database-backed operations for repository records."""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(
        self, payload: RepositoryRecordCreate
    ) -> RepositoryRecordResponse:
        record = RepositoryRecord(
            repo_name=payload.repo_name,
            docker_name=payload.docker_name,
        )
        self.session.add(record)
        await self.session.commit()
        await self.session.refresh(record)
        return RepositoryRecordResponse.model_validate(record)

    async def list_all(self) -> list[RepositoryRecordResponse]:
        result = await self.session.execute(
            select(RepositoryRecord).order_by(RepositoryRecord.id)
        )
        records = result.scalars().all()
        return [RepositoryRecordResponse.model_validate(record) for record in records]

    async def get_by_repo_name(self, repo_name: str) -> RepositoryRecord:
        result = await self.session.execute(
            select(RepositoryRecord).where(RepositoryRecord.repo_name == repo_name)
        )
        record = result.scalar_one_or_none()
        if record is None:
            raise NotFoundException(f"Repository '{repo_name}' was not found in the database.")
        return record
