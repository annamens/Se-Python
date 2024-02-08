import os
import configparser

config = configparser.ConfigParser()
print('config path: ', os.getcwd())
config.read(os.path.join(os.getcwd(), "config.ini"))


class ReadConfig:
    @staticmethod
    def getAppUrl():
        # url= config['common_info']['baseURL']
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        userName = config.get('common info', 'username')
        return userName

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getBrowser():
        browser = config.get('common info', 'browser')
        return browser

