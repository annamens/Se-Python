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