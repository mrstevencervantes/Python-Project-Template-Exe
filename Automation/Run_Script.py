"""Main file to run script. Please see README.md and config file for more info."""

import csv
import logging
import traceback
from pathlib import Path
from datetime import datetime
from typing import Any, Union, Final

from Config.project_setup import ConfigSetup

# Setup main logger
logger = logging.getLogger("main")


def main(data: dict[str, Any]) -> None:
    """Main function to be run."""

    logger.debug(f"Starting main function.")
    successful_run: bool = False
    PARENT_DIRECTORY: Final[Path] = data.pop("parent_dir")

    try:
        logger.critical(f"Replace this with the actual function you want to run.\n{data}")
    except Exception as e:
        logger.exception(
            f"A fatal error has occured during this run. {str(e)} Please review the debugger log and the Error Stack Trace text file.")
        log_exception(PARENT_DIRECTORY / str(config.get("ErrorOutput")))
    else:
        successful_run = True
        logger.debug("No errors during automation run.")
    finally:
        try:
            write_log(data, PARENT_DIRECTORY, successful_run)
        except Exception as e:
            logger.exception(
                f"A fatal error has occured while attempting to log details of this run. {type(e).__name__} {str(e)} Unable to write log.")

    logger.debug(f"Main function completed.")


def write_log(config: dict[str, Any], parent_dir: Path, successful_run: bool) -> None:
    """Write output of current run to log file."""

    # Declare variables
    SCRIPT_NAME: Final[str] = config.get("ScriptName", parent_dir.name)
    LOG_FILE_PATH: Final[Path] = parent_dir / str(config.get("LogFile"))
    HEADER_ROW: Final[list[str]] = ["Script Name", "Date/Time Run", "Username", "Successful?"]

    # If file does not exist, create it and write the header row
    if not LOG_FILE_PATH.is_file():
        with open(LOG_FILE_PATH, mode='w', newline='') as log_file:
            log_file_writer = csv.writer(log_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            log_file_writer.writerow(HEADER_ROW)

    # Append content to the CSV file
    with open(LOG_FILE_PATH, mode='a', newline='') as log_file:
        log_file_writer = csv.writer(log_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        log_file_writer.writerow([SCRIPT_NAME, datetime.now(), config.get("username"), str(successful_run)])


def log_exception(filename: Path) -> None:
    """Write out exceptions to file path provided."""

    logger.info("Writing error to file.")
    try:
        with open(filename, "w") as f:
            f.write(f"{datetime.now()}\n")
            f.write(traceback.format_exc())
    except FileNotFoundError as e:
        logger.error(str(e))
    except Exception as e:
        logger.critical(f"An unexpected error occurred. {type(e).__name__} {str(e)} Please review logs. Unable to continue.")
    else:
        logger.info("Error writing completed.")


if __name__ == "__main__":
    config = ConfigSetup()
    config_data: dict[str, Any] = config.setup_dict()
    script_name: Union[str, Path] = config_data.get("ScriptName", config_data.get("parent_dir").name)
    logger.info(f"Starting {script_name} automation...")
    main(config_data)
    logger.info("Automation completed.")
