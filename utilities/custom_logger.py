import logging
import os

log_dir = "logs.log"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


def setup_logger(name, log_file, level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

error_logger = setup_logger('error_logger', os.path.join(log_dir, 'error.log'), level=logging.ERROR)
exception_logger = setup_logger('exception_logger', os.path.join(log_dir, 'exception.log'), level=logging.ERROR)
test_logger = setup_logger('test_logger', os.path.join(log_dir, 'test.log'), level=logging.INFO)


# Example usage
# def log_demo():
#     try:
#         x = 1 / 0
#     except ZeroDivisionError as e:
#         exception_logger.error("Exception occurred", exc_info=True)
#         error_logger.error("Zero Division Error occurred")
#
#     test_logger.info("This is an info message for tests")
#     test_logger.error("This is an error message for tests")
#
#
# if __name__ == "__main__":
#     log_demo()
