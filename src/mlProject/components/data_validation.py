import os   # Handles file operations.
from mlProject import logger # Logs messages (assumed to be a custom logging module in mlProject).
from mlProject.entity.config_entity import DataValidationConfig # A configuration entity containing paths and schema details.
import pandas as pd # Reads and processes the CSV dataset.

# Accepts a configuration object (DataValidationConfig) containing: unzip_data_dir: Path to the dataset file.,STATUS_FILE: Path to store validation results.,all_schema: Dictionary containing expected column names and data types.
class DataValiadtion:   
    def __init__(self, config: DataValidationConfig):
        self.config = config

#  Column Validation
    def validate_all_columns(self)-> bool: 
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir) #Reads the dataset into a pandas DataFrame.
            all_cols = list(data.columns) # Extracts the column names from the dataset (all_cols).

            all_schema = self.config.all_schema.keys()  # Extracts the expected column names from the schema (all_schema).

            #  Checking for Missing or Extra Columns
            for col in all_cols:   # Iterates through the actual dataset columns (all_cols) 
                if col not in all_schema: #Checks if each column is present in the expected schema (all_schema).
                    validation_status = False   # If a column is missing, writes False to STATUS_FILE.
                    with open(self.config.STATUS_FILE, 'w') as f:  
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True # If the column is valid, writes True to STATUS_FILE.
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        # If an error occurs, it is raised without logging or handling.
        except Exception as e:
            raise e

