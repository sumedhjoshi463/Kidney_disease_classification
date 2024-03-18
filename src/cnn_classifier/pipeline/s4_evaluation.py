from cnn_classifier.config.configuration import ConfigurationManager
from cnn_classifier.componants.evaluation import Evaluation 
from cnn_classifier import logger

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            evaluation = Evaluation(eval_config)
            evaluation.evaluation()
            evaluation.log_mlflow()
        except Exception as e:
            raise e



if __name__ == "__main":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage Evaluation started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage Evaluation completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e