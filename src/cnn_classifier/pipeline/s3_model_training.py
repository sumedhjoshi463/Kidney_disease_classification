from cnn_classifier.config.configuration import ConfigurationManager
from cnn_classifier.componants.model_training import Training
from cnn_classifier import logger

STAGE_NAME = "Training Phase"

class TrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            training_config = config.get_training_config()
            training = Training(training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()

        except Exception as e:
            raise e

    

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e