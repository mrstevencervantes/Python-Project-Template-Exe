"""Convert JSON file into a dictionary that can be passed to other modules for later use."""

import json
from pathlib import Path
from typing import Final, Union

from jsonschema import validate
from jsonschema.exceptions import ValidationError


def config_json(json_path: str='Config/Config.json', schema_path: str='Config/config-schema.json') -> dict[str, Union[str, bool, Path]]:
    """Read JSON configuration file, validate the file with the JSON schema and create final configuration dictionary.
    Parameters: json_path (str) - path to JSON file used for configuration setup.
                json_schema (str) - path to JSON file used for validating JSON file use for setup."""

    # Build current working directory and file paths
    WORKING_DIR: Final[Path] = create_working_directory()
    JSON_FILE: Final[Path] = Path.joinpath(WORKING_DIR, json_path)
    SCHEMA_FILE: Final[Path] = Path.joinpath(WORKING_DIR, schema_path)
    JSON_DATA: Final[dict[str, Union[str, bool, Path]]] = {}
    SCHEMA: Final[dict[str, Union[str, bool, Path]]] = {}

    try:
        # Read in JSON file
        with open(JSON_FILE) as f:
            JSON_DATA.update(json.load(f))

        # Read in JSON schema
        with open(SCHEMA_FILE) as f:
            SCHEMA.update(json.load(f))
    except FileNotFoundError:
        raise

    # Validate JSON schema, raise exception if invalid
    try:
        validate(instance=JSON_DATA, schema=SCHEMA)
    except ValidationError:
        raise

    # Create file paths for later use
    CONFIG_FILE: Final[Path] = Path.joinpath(WORKING_DIR, str(JSON_DATA.pop("config_path")))
    LOGGER_FILE: Final[Path] = Path.joinpath(WORKING_DIR, str(JSON_DATA.pop("logger_path")))

    # Make sure all file paths are valid, raise exception if not
    if not CONFIG_FILE.is_file():
        raise FileNotFoundError(f"Config file not found: {CONFIG_FILE}")
    
    if not LOGGER_FILE.is_file():
        raise FileNotFoundError(f"Logger config file not found: {LOGGER_FILE}")

    # Create file paths for later use
    JSON_DATA["config_path"] = CONFIG_FILE
    JSON_DATA["logger_path"] = LOGGER_FILE
    JSON_DATA["work_dir"] = WORKING_DIR
    JSON_DATA["parent_dir"] = WORKING_DIR.parent

    return JSON_DATA


def create_working_directory() -> Path:
    TEMP: Final[list[str]] = []
    for part in Path.cwd().parts:
        TEMP.append(part)
        if part.lower() == "automation":
            break
    return Path("/".join(TEMP))


if __name__ == "__main__":
    json_data: dict[str, Union[str, bool, Path]] = config_json('Config/Config.json', 'Config/config-schema.json')
