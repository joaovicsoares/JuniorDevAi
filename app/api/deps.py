"""
Shared FastAPI dependencies (auth, database sessions, etc.)

Import these in your endpoint files via:
    from app.api.deps import get_db
"""

# from app.core.config import settings


# Example: database session dependency (uncomment when you add a DB)
# async def get_db():
#     async with async_session() as session:
#         yield session
