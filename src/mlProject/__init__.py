import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"    ## create log dir/folder ate src
log_filepath = os.path.join(log_dir,"running_logs.log")   ## save log file in logs folder 
os.makedirs(log_dir, exist_ok=True)  ## create log dir/folder ate src


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),   #### FileHandler is used in the logging module to write log messages to a file instead of the console.

        logging.StreamHandler(sys.stdout)    #### StreamHandler is used in Python’s logging module to send log messages to the console (stdout/stderr) instead of a file.
    ]
)

logger = logging.getLogger("mlProjectLogger")    #### Initialize logs