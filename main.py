from src.cnn_classifier import logger
# from cnn_classifier.pipeline.s1_data import DataIngestionPipeline
# from cnn_classifier.pipeline.s2_base_model import PrepareBaseModelTrainingPipeline
from cnn_classifier.pipeline.s3_model_training import TrainingPipeline
from cnn_classifier.config.configuration import ConfigurationManager

# try:
#     logger.info('Starting data ingestion pipeline')
#     obj = DataIngestionPipeline()
#     obj.main()
#     logger.info(" data ingestion stage is finished")
# except Exception as e :
#     raise e

# STAGE_NAME = "Prepare base model" 
# try:
#     logger.info(f"*******************")
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     obj = PrepareBaseModelTrainingPipeline()
#     obj.main()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exception(e)
#     raise e

STAGE_NAME = "Training Phase" 
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = TrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e