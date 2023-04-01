import logging
import os

log_filename = "test.log"
if os.path.exists(log_filename):
    os.remove(log_filename)

# create a Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler and set the logging level
file_handler = logging.FileHandler(log_filename)
file_handler.setLevel(logging.INFO)

# create a formatter and add it to the file handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# add the file handler to the logger
logger.addHandler(file_handler)


def log_step(message: str):
    """
    add test steps to log
    """
    logger.info(f"Test step: {message}")
