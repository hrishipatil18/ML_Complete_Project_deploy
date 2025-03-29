from mlProject.constants import *    #### get Yaml file paths from  mlProject/constants/__init__.py

# read yaml configuration and Ensures required directories exist. from mlProject/utils/common.py
from mlProject.utils.common import read_yaml, create_directories 

#A data class that defines ingestion parameters.
## Returning a structured DataIngestionConfig entity for data ingestion and DataValidationConfig for validation.
from mlProject.entity.config_entity import (DataIngestionConfig, 
                                            DataValidationConfig)

class ConfigurationManager:                                  
    def __init__(
        self,
config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath) # Reads main config
        self.params = read_yaml(params_filepath) # Reads model parameters
        self.schema = read_yaml(schema_filepath) # Reads data schema

        create_directories([self.config.artifacts_root])  # Ensures artifacts directory exists


    def get_data_ingestion_config(self) -> DataIngestionConfig:       
        config = self.config.data_ingestion   # Extracts data_ingestion settings from config.yaml.
        
        create_directories([config.root_dir])  # Creates the required root_dir.

         # Returns an instance of DataIngestionConfig  containing: root_dir, source_URL , local_data_file unzip_dir. 
    
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation  #Retrieves the data_validation settings from config.yaml
        schema = self.schema.COLUMNS  # Extracts the expected column schema from schema.yaml.

        create_directories([config.root_dir]) # Ensures that the root directory for data validation exists. Calls create_directories() to create the directory if it doesn’t exist.
        # Stores the validation settings in a structured dataclass 
        data_validation_config = DataValidationConfig(   
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

    return data_validation_config
    