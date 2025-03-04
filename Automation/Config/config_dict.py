"""Convert workbook data into a dictionary that can be passed to other modules for later use."""

import csv
import getpass
import logging
from pathlib import Path
from typing import Final, Union, Any

import pandas as pd

# Create logger
logger: logging.Logger = logging.getLogger("main")


def config_data(json_data: dict[str, Union[str, bool, Path]]) -> dict[str, Any]:
    """Read config workbook based on file type and create a dictionary."""

    # Define file paths and create return dictionary
    CONFIG_PATH: Final[Path] = Path(str(json_data.pop("config_path")))
    data: dict[str, Any] = {}

    if CONFIG_PATH.suffix == ".csv":
        with open(CONFIG_PATH, "r") as f:
            temp = csv.DictReader(f)
            data.update({line["Setting"]: line["value"] for line in temp})

    if CONFIG_PATH.suffix == ".xlsx":
        constants_df = pd.read_excel(CONFIG_PATH, "Constants", header=0)
        constants_df = constants_df.dropna(subset=["Constant Value"], how="any")
        constants_df = constants_df[constants_df["Constant Value"] != ''] 
        constants_dict = dict(zip(constants_df["Constant Name"], constants_df["Constant Value"]))

        settings_sheet = f'{constants_dict.pop("Environment")} Settings'
        settings_df = pd.read_excel(CONFIG_PATH, settings_sheet, header=0)
        settings_df = settings_df.dropna(subset=["Setting Value"], how="any")
        settings_df = settings_df[settings_df["Setting Value"] != ''] 
        settings_dict = dict(zip(settings_df["Setting Name"], settings_df["Setting Value"]))

    data = {**settings_dict, **constants_dict, **json_data}
    data['username'] = getpass.getuser()
    return data

if __name__ == "__main__":
    from config_json import config_json
    from logger_module import logger_setup
    JSON_DATA: dict[str, Union[str, bool, Path]] = config_json()
    logger = logger_setup(JSON_DATA)
    data: dict[str, Any] = config_data(JSON_DATA)
    logger.debug(f"dictionary data: {data}")
