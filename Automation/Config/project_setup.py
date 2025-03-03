"""Setup project configuration."""

import logging
from typing import Any
from dataclasses import dataclass, field

from Config.config_json import config_json
from Config.logger_module import logger_setup
from Config.config_dict import config_data

@dataclass
class ConfigSetup:
    """Setup project configuration. 
    Parameters: json_path (str) - path to JSON file used for configuration setup.
                json_schema (str) - path to schema file used for validating JSON file during setup.
    """
    
    json_path: str = 'Config/Config.json'
    json_schema_path: str = 'Config/config-schema.json'
    logger: logging.Logger = field(init=False, repr=False)

    def __post_init__(self) -> None:
        """Initialize logger on instance creation."""
        self.logger = logging.getLogger("main")

    def _config_setup(self, json_path: str, json_schema_path: str) -> dict[str, Any]:
        """Read and parse JSON configuration file using JSON schema."""

        try:
            return config_json(self.json_path, self.json_schema_path)
        except FileNotFoundError:
            raise
        except Exception as e:
            raise Exception(f"Error setting up JSON config: {type(e).__name__} {str(e)}")

    def _logger_setup(self, json_data: dict[str, Any]) -> None:
        """Create main logger for project."""

        if not self.logger.hasHandlers() and json_data.items():
            try:
                self.logger = logger_setup(json_data)
            except FileNotFoundError:
                raise
            except Exception as e:
                raise Exception(f"Error setting up logger: {type(e).__name__} {str(e)}")

    def setup_dict(self) -> dict[str, Any]:
        """Create final dictionary of configuration settings."""

        json_data: dict[str, Any] = self._config_setup(self.json_path, self.json_schema_path)
        self._logger_setup(json_data)

        try:
            return config_data(self.json_data)
        except FileNotFoundError:
            raise
        except Exception as e:
            raise Exception(f"Error setting up config data: {type(e).__name__} {str(e)}")
