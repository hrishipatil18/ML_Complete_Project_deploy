import os  # File and directory operations
import urllib.request as request # Downloads files from a URL.
import zipfile # Extracts ZIP archives.
from mlProject import logger #Logs status messages. 
from mlProject.utils.common import get_size # Utility function to check file size.
from pathlib import Path  # File and directory operations
from mlProject.entity.config_entity import (DataIngestionConfig) # Stores configuration parameters.

# Accepts DataIngestionConfig to get paths & URLs dynamically.
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):  
        self.config = config


    
    def download_file(self):      #downloading data from url
        if not os.path.exists(self.config.local_data_file):  #Checks if the file exists → If not, it downloads it.
            filename, headers = request.urlretrieve(    # Uses request.urlretrieve() to fetch the file.
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}") # Logs details of the download or file size if it exists.
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  # Logs details of the download or file size if it exists.



    def extract_zip_file(self):    #Unzip data
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True) # Creates an extraction directory if it doesn’t exist.
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path) # Uses zipfile.ZipFile.extractall() to extract contents.
  