"""Create logger which can be passed to other modules."""

import logging.config
from pathlib import Path
from typing import Final, Union, Any

import yaml
from colorlog import ColoredFormatter


def logger_setup(json_data: dict[str, Union[str, bool, Path]]) -> logging.Logger:
    """Create logger which can be passed to other modules.
    Parameters: json_data (dict) - dictionary of initialization values."""

    # Declare return dictionary
    CONFIG_DICT: Final[dict[str, Any]] = {}
    
    # Create the 'Log' folder if it doesn't exist
    LOGGER_FOLDER: Final[Path] = Path(str(json_data.get("work_dir")), str(json_data.get("log_path")))
    LOGGER_FOLDER.mkdir(exist_ok=True)

    # Read in logger config yaml file with safe load
    with open(json_data.pop("logger_path"), 'r') as f:
        CONFIG_DICT.update(yaml.safe_load(f))

    # Update logger file path to include the working directory
    LOG_FILE_PATH: Final[Path] = json_data.get("work_dir") / CONFIG_DICT["handlers"]["file"]["filename"]

    # Create the debugging_file.log if it doesn't exist
    if not LOG_FILE_PATH.exists():
        with open(LOG_FILE_PATH, 'w'):
            pass

    # Update logger configuration with the new file path
    CONFIG_DICT["handlers"]["file"]["filename"] = LOG_FILE_PATH

    # Set up console logging based on config_json, set False if not found
    if json_data.pop("logging_colors", False):
        CONFIG_DICT['handlers']['console']['formatter'] = 'colorFormatter'

        # Create color formatter for console output
        color_formatter = ColoredFormatter(
            CONFIG_DICT["formatters"]['colorFormatter']['format'],
            log_colors=CONFIG_DICT["formatters"]['colorFormatter']['log_colors'],
            reset=True,
        )

        # Update console handler with the color formatter
        CONFIG_DICT['handlers']['console']['formatter'] = 'color'
        CONFIG_DICT['formatters']['color'] = {
            '()': color_formatter.__class__,
            'format': color_formatter._fmt,
            'log_colors': color_formatter.log_colors
        }
    else:
        CONFIG_DICT['handlers']['console']['formatter'] = 'consoleFormatter'

    # create logger
    logging.config.dictConfig(CONFIG_DICT)
    logger: Final[logging.Logger] = logging.getLogger("main")
    return logger

if __name__ == "__main__":
    from config_json import config_json
    JSON_DATA: dict[str, Union[str, bool, Path]] = config_json()
    logger = logger_setup(JSON_DATA)
