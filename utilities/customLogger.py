import logging
import os


class LogGen:
    @staticmethod
    def logGen():
        print(os.getcwd())
        path = os.getcwd()
        logging.basicConfig(filename = (os.path.join(path, "automation.log")),
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt= '%m/%d/%Y %I:%M:%S %p',force=True)
        logger =logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


import logging
import os
from logging.handlers import RotatingFileHandler


# Create a function to set up the custom logger
def setup_custom_logger(name):
    # Create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create log directory if it does not exist
    log_directory = 'logs'
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Create handlers
    error_handler = RotatingFileHandler(f'{log_directory}/errors.log', maxBytes=1000000, backupCount=3)
    exception_handler = RotatingFileHandler(f'{log_directory}/exceptions.log', maxBytes=1000000, backupCount=3)
    failed_test_handler = RotatingFileHandler(f'{log_directory}/failed_tests.log', maxBytes=1000000, backupCount=3)

    # Set level for handlers
    error_handler.setLevel(logging.ERROR)
    exception_handler.setLevel(logging.ERROR)
    failed_test_handler.setLevel(logging.WARNING)  # Assuming failed tests are logged as warnings

    # Create formatters and add it to handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    error_handler.setFormatter(formatter)
    exception_handler.setFormatter(formatter)
    failed_test_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(error_handler)
    logger.addHandler(exception_handler)
    logger.addHandler(failed_test_handler)

    return logger


# Custom function to log exceptions
def log_exception(logger, exception):
    logger.exception("Exception occurred: ", exc_info=exception)


# Example usage
if __name__ == "__main__":
    # Set up custom logger
    logger = setup_custom_logger('my_logger')

    try:
        # Simulate an error
        1 / 0
    except ZeroDivisionError as e:
        log_exception(logger, e)
        logger.error("This is an error message")

    # Log a failed test
    logger.warning("Test case XYZ failed due to assertion error")
