"""Setup project configuration."""

from Config.config_json import config_json
from Config.logger_module import logger_setup
from Config.config_dict import config_data

class ConfigSetup(object):
    def __init__(self, json_path: str='Config/Config.json') -> None:
        """Setup project configuration. Parameters: json_path (str) - path to JSON file used for configuration setup."""
        self.json_path = json_path
        self.json_data = None
        self.config_data = None
        self.logger = None

    def _config_setup(self) -> None:
        """Read and parse JSON file."""

        if self.json_data is None:
            try:
                self.json_data = config_json(self.json_path)
            except FileNotFoundError:
                raise
            except Exception as e:
                raise Exception(f"Error setting up JSON config: {type(e).__name__} {str(e)}")

    def _logger_setup(self) -> None:
        """Create main logger for project."""

        if self.logger is None and self.json_data:
            try:
                self.logger = logger_setup(self.json_data)
            except FileNotFoundError:
                raise
            except Exception as e:
                raise Exception(f"Error setting up logger: {type(e).__name__} {str(e)}")

    def setup_dict(self) -> dict:
        """Create dictionary of configuration settings."""

        self._config_setup()
        self._logger_setup()

        try:
            if self.config_data is None and self.json_data:
                self.config_data = config_data(self.json_data)
            return self.config_data
        except FileNotFoundError:
            raise
        except Exception as e:
            raise Exception(f"Error setting up config data: {type(e).__name__} {str(e)}")
