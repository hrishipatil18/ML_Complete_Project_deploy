import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
 
""" we make logging structure / basic config that what we can see in logs so in logging.basicConfig => 
level = logging.INFO means which kind of loggs error info debug we want to print =>
format =  '[%(asctime)s]:%(message)s:' means we want stamp time and error message as logs 
eg. logging.info(f"Creating directory; {filedir} for the file: {filename} """

project_name = "mlProject"


list_of_files = [
    ".github/workflows/.gitkeep", #Because wont take empty file while commiting
    f"src/{project_name}/__init__.py",  ##contains main sricpts
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",   ## contains all configuration
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"


]


for filepath in list_of_files:
    filepath = Path(filepath)       ## create path of file eg. src\mlProject\__init__.py
    filedir, filename = os.path.split(filepath)  #split file dir (src\mlProject\components) and file in it (__init__.py). like filedir => .github\workflows filename =>.gitkeep


    if filedir !="":
        ## if file dir not empty then create dir
        os.makedirs(filedir, exist_ok=True)  
        #logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):   ### this is for Creating empty file: main.py or Creating empty file: src\mlProject\entity\__init__.py:
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")