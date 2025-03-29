from mlProject.config.configuration import ConfigurationManager   # Fetches configurations from YAML files.
from mlProject.components.data_ingestion import DataIngestion   # Handles data downloading and extraction.
from mlProject import logger  # Logs the process for debugging.



STAGE_NAME = "Data Ingestion stage"   # Used for structured logging messages.

class DataIngestionTrainingPipeline:
    def __init__(self):   
        pass

    def main(self):
        # Creates an instance of ConfigurationManager to read configurations.
        config = ConfigurationManager()
        # Fetches DataIngestionConfig (paths, URLs, directories).
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        # Runs download_file() and extract_zip_file() to fetch and extract data. 
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


    
if __name__ == '__main__':
    try:   # Handles errors with try-except to catch failures.
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")  #  Logs the start and completion of the ingestion stage.
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x") 
    except Exception as e:  #  Raises exceptions if anything goes wrong
        logger.exception(e)
        raise e
