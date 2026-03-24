from urllib.parse import urlparse

from app.core.exceptions import BadRequestException
from app.schemas.repository import RepositoryLinkResponse


class RepositoryService:
    """Business logic for validating and normalizing repository links."""

    def parse_github_repo_url(self, repo_url: str) -> RepositoryLinkResponse:
        parsed_url = urlparse(repo_url)
        host = (parsed_url.netloc or "").lower()

        if host not in {"github.com", "www.github.com"}:
            raise BadRequestException("Only github.com repository links are supported.")

        path_parts = [part for part in parsed_url.path.split("/") if part]
        if len(path_parts) < 2:
            raise BadRequestException(
                "The URL must include both the repository owner and name."
            )

        owner, repository = path_parts[0], path_parts[1]

        if repository.endswith(".git"):
            repository = repository[:-4]

        reserved_paths = {
            "about",
            "codespaces",
            "collections",
            "contact",
            "events",
            "explore",
            "features",
            "issues",
            "join",
            "login",
            "marketplace",
            "notifications",
            "organizations",
            "orgs",
            "pricing",
            "pulls",
            "search",
            "settings",
            "site",
            "sponsors",
            "topics",
            "trending",
        }
        if owner.lower() in reserved_paths:
            raise BadRequestException("The URL does not point to a GitHub repository.")

        normalized_repo_url = f"https://github.com/{owner}/{repository}"

        return RepositoryLinkResponse(
            provider="github",
            owner=owner,
            repository=repository,
            repo_url=normalized_repo_url,
            clone_url=f"{normalized_repo_url}.git",
            api_url=f"https://api.github.com/repos/{owner}/{repository}",
        )
