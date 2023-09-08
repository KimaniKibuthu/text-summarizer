import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from components.data_transformation import DataTransformation
from config.config import ConfigurationManager
from entity import DataTransformationConfig
from loging import logger
from constants.constants import CONFIG_PATH, PARAMS_PATH
from datasets import Dataset, DatasetDict, load_from_disk

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            logger.info(">>>>> stage: data_transformation")
            config_manager = ConfigurationManager(CONFIG_PATH, PARAMS_PATH)
            data_transformation_config = config_manager.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config)
            data_transformation.transform_data_to_transformers_format()
            data_transformation.convert_to_features()
            logger.info("stage completed successfully")
        except Exception as e:
            logger.error(e)
            raise e