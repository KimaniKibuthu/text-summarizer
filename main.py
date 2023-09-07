import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.loging import logger
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

logger.info("Running pipeline...")
logger.info(">>>>> stage_01_data_ingestion started")    

try:
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info("<<<<< stage_01_data_ingestion completed\n")
except Exception as e:
    logger.error(e)
    raise e

logger.info(">>>>> stage_01_data_ingestion started")

try:
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info("<<<< stage_01_data_validation completed\n")
except Exception as e:
    logger.error(e)
    raise e