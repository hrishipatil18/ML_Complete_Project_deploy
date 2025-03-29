from mlProject.config.configuration import ConfigurationManager  # Loads configuration settings (like dataset path, schema).
from mlProject.components.data_validation import DataValiadtion  # Class responsible for validating dataset columns.
from mlProject import logger #  Logs messages for debugging and tracking.


STAGE_NAME = "Data Validation stage"  # This variable stores the pipeline stage name, making logs more readable.

# A simple pipeline class to orchestrate the data validation step.
class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager() # Loads configuration
        data_validation_config = config.get_data_validation_config() # Retrieves validation settings
        data_validation = DataValiadtion(config=data_validation_config) # Creates an instance of DataValiadtion 
        data_validation.validate_all_columns() # Runs column validation





if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

