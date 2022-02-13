"""This module provides the RP To-Do config functionality."""
import configparser
from pathlib import Path

import typer

from pyfly import DB_READ_ERROR, DB_WRITE_ERROR, DIR_ERROR, FILE_ERROR, SUCCESS, __app_name__

CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__))
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.ini"

from pyfly.database import AsyncDatabaseHandler


def init_app(db_path: str) -> int:
    """Initialize the application."""
    config_code = _init_database()
    if config_code != SUCCESS:
        return config_code
    return SUCCESS

def _init_database() -> int:
    """Initialize DB by getting one entry from Response table."""
    try:
        asdb = AsyncDatabaseHandler()
        try:
            if not asdb.run("get_response"):
                typer.secho(
                f'Creating database failed with "{DB_READ_ERROR}"',
                fg=typer.colors.RED,
            )
        except Exception as e:
            raise typer.Exit(1) from e
    except OSError:
        return DB_READ_ERROR
    return SUCCESS