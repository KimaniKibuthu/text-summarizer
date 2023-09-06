import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from components.data_ingestion import DataIngestion
from config.config import ConfigurationManager
from loging import logger




class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        logger.info(">>>>> stage_01_data_ingestion started")
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.run()
        logger.info("<<<<< stage_01_data_ingestion completed\n")
