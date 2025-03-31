from mlProject import logger  # Used for logging pipeline execution progress.
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline # Runs the data ingestion stage.
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline # Runs the data validation stage.
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline # Runs the data Transformation stage.
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline # Runs the training.
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline # Runs the Evalution.

STAGE_NAME = "Data Ingestion stage" #  Helps in structured logging for better debugging.
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")  # Logs the start of Data Ingestion.
   # Creates an instance of DataIngestionTrainingPipeline and runs it.
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   # Logs completion of Data Ingestion.
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# Handles exceptions to catch errors and log them properly.
except Exception as e: 
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataTransformationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelEvaluationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e