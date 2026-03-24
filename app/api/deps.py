"""
Shared FastAPI dependencies (auth, database sessions, etc.)

Import these in your endpoint files via:
    from app.api.deps import get_db
"""

from app.db.session import get_db
