from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class RepositoryRecord(Base):
    """Stored repository metadata used by the API."""

    __tablename__ = "repository_records"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    repo_name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    docker_name: Mapped[str] = mapped_column(String(255), nullable=False)
