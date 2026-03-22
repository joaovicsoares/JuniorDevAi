"""
SQLAlchemy model definitions.

When you're ready to add a database, define your models here.
Example:

    from sqlalchemy import Column, Integer, String, Text
    from app.models.base import Base

    class Dataset(Base):
        __tablename__ = "datasets"

        id = Column(Integer, primary_key=True, index=True)
        name = Column(String(255), nullable=False)
        description = Column(Text, nullable=True)
"""
