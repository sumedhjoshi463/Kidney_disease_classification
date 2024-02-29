from cnn_classifier.config.configuration import ConfigurationManager
from cnn_classifier.componants.data_ingestion import DataIngestion
from cnn_classifier.constants import *
from cnn_classifier import logger

STAGE_NAME = 'data_ingestion_stage'

class DataIngestionPipeline:
    def __init__(self):
        pass

    try:
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        # data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    except Exception as e:
        raise e




if __name__ == '__main__':
    try:
        logger.info('Starting data ingestion pipeline')
        obj = DataIngestionPipeline()
        obj.main()
        logger.info("stage is finished")
    except Exception as e :
        raise e
