import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from components.data_validation import DataValidation
from config.config import ConfigurationManager
from loging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        logger.info(">>>>> stage_02_data_validation started")
        config_manager = ConfigurationManager()
        data_validation_config = config_manager.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_files()
        logger.info("<<<<< stage_01_data_validation completed\n")
    

