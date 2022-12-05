import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getAppUrl():
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

