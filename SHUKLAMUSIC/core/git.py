import asyncio
import shlex
from typing import Tuple
import os  # added for Heroku check

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

import config

from ..logging import LOGGER


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(install_requirements())


def git():
    """
    Initialize Git repository and fetch updates.
    Heroku-safe: skips Git operations if running on Heroku.
    Supports optional GitHub token authentication.
    """
    # --- Heroku-safe: skip Git operations ---
    if os.environ.get("DYNO"):
        LOGGER(__name__).info("Running on Heroku. Skipping Git operations.")
        return

    # --- Prepare repository URL with token ---
    REPO_LINK = config.UPSTREAM_REPO
    if config.GIT_TOKEN:
        try:
            GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
            TEMP_REPO = REPO_LINK.split("https://")[1]
            UPSTREAM_REPO = f"https://{GIT_USERNAME}:{config.GIT_TOKEN}@{TEMP_REPO}"
        except Exception:
            UPSTREAM_REPO = config.UPSTREAM_REPO
            LOGGER(__name__).warning(
                "Failed to construct tokenized repo URL. Using plain URL."
            )
    else:
        UPSTREAM_REPO = config.UPSTREAM_REPO

    # --- Initialize or fetch repository ---
    try:
        repo = Repo()
        LOGGER(__name__).info("Git Client Found [VPS DEPLOYER]")
    except GitCommandError:
        LOGGER(__name__).info("Invalid Git Command")
    except InvalidGitRepositoryError:
        LOGGER(__name__).info("No Git repository found. Initializing a new one...")
        repo = Repo.init()
        if "origin" in [r.name for r in repo.remotes]:
            origin = repo.remote("origin")
        else:
            origin = repo.create_remote("origin", UPSTREAM_REPO)

        try:
            origin.fetch()
        except GitCommandError as e:
            LOGGER(__name__).warning(f"Git fetch failed: {e}")
            return

        # --- Branch setup ---
        repo.create_head(
            config.UPSTREAM_BRANCH,
            origin.refs[config.UPSTREAM_BRANCH],
        )
        repo.heads[config.UPSTREAM_BRANCH].set_tracking_branch(
            origin.refs[config.UPSTREAM_BRANCH]
        )
        repo.heads[config.UPSTREAM_BRANCH].checkout(True)

        # --- Ensure origin exists and pull safely ---
        try:
            repo.create_remote("origin", config.UPSTREAM_REPO)
        except BaseException:
            pass
        nrs = repo.remote("origin")
        try:
            nrs.fetch(config.UPSTREAM_BRANCH)
        except GitCommandError:
            LOGGER(__name__).warning("Fetch from origin failed.")
        try:
            nrs.pull(config.UPSTREAM_BRANCH)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
            LOGGER(__name__).info("Reset hard to FETCH_HEAD after pull failure.")

        # --- Install requirements ---
        install_req("pip3 install --no-cache-dir -r requirements.txt")
        LOGGER(__name__).info("Fetching updates from upstream repository completed.")
