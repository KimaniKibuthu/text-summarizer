import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from constants.constants import CONFIG_PATH, PARAMS_PATH
from loging import logger
from utils.common import get_size
from utils.common import read_yaml
from entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_PATH,
        params_filepath = PARAMS_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
 

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
