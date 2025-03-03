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
                json_schema (str) - path to schema file used for validating JSON file during setup."""
    json_path: str = 'Config/Config.json'
    json_schema: str = 'Config/config-schema.json'
    json_data: dict[str, Any] = field(default_factory=dict)
    config_data: dict[str, Any] = field(default_factory=dict)

    def _config_setup(self) -> None:
        """Read and parse JSON configuration file using JSON schema."""

        if not self.json_data.items():
            try:
                self.json_data: dict[str, Any] = config_json(self.json_path, self.json_schema)
            except FileNotFoundError:
                raise
            except Exception as e:
                raise Exception(f"Error setting up JSON config: {type(e).__name__} {str(e)}")

    def _logger_setup(self) -> None:
        """Create main logger for project."""

        if not hasattr(ConfigSetup, "logger") and self.json_data.items():
            try:
                self.logger: logging.Logger = logger_setup(self.json_data)
            except FileNotFoundError:
                raise
            except Exception as e:
                raise Exception(f"Error setting up logger: {type(e).__name__} {str(e)}")

    def setup_dict(self) -> dict[str, Any]:
        """Create final dictionary of configuration settings."""

        self._config_setup()
        self._logger_setup()

        try:
            if not self.config_data.items() and self.json_data.items():
                self.config_data = config_data(self.json_data)
            return self.config_data
        except FileNotFoundError:
            raise
        except Exception as e:
            raise Exception(f"Error setting up config data: {type(e).__name__} {str(e)}")
