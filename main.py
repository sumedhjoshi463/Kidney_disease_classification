from src.cnn_classifier import logger
from cnn_classifier.pipeline.s1_data import DataIngestionPipeline


try:
    logger.info('Starting data ingestion pipeline')
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(" data ingestion stage is finished")
except Exception as e :
    raise e