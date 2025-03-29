from mlProject import logger  # Used for logging pipeline execution progress.
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline # Runs the data ingestion stage.

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

