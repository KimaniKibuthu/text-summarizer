import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from constants.constants import CONFIG_PATH, PARAMS_PATH
from loging import logger
from utils.common import get_size
from utils.common import read_yaml
from entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelEvaluationConfig

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
            local_data_file=config.local_data_dir,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config

    def get_data_validation_config(self):
        
        return DataValidationConfig(
            root_dir = Path(self.config["data_validation"]["root_dir"]),
            STATUS_FILE = self.config["data_validation"]["STATUS_FILE"],
            ALL_REQUIRED_FILES = self.config["data_validation"]["ALL_REQUIRED_FILES"]
        )
        
    def  get_data_transformation_config(self):
        return DataTransformationConfig(
            root_dir = Path(self.config["data_transformation"]["root_dir"]),
            data_path = Path(self.config["data_transformation"]["data_path"]),
            tokenizer_name = self.config["data_transformation"]["tokenizer_name"]
        ) 
        
    def get_model_evaluation_config(self):
        return ModelEvaluationConfig(
            root_dir = Path(self.config["model_evaluation"]["root_dir"]),
            data_dir= Path(self.config["model_evaluation"]["data_dir"]),
            model_path = Path(self.config["model_evaluation"]["model_path"]),
            tokenizer_path=self.config["model_evaluation"]["tokenizer_path"]
        )  
