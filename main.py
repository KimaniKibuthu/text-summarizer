from src.loging import logger
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

logger.info("Running pipeline...")
logger.info(">>>>> stage_01_data_ingestion started")    

try:
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info("<<<<< stage_01_data_ingestion completed\n")
except Exception as e:
    logger.error(e)
    raise e
