import configparser

parser = configparser.RawConfigParser()
parser.read("C:\\Users\\arist\\PycharmProjects\\OpenCartE2E\\Configurations\\Config.ini")


class Read_Config:

    @staticmethod
    def Get_App_URL():
        return parser.get("Env Details", "URL")

    @staticmethod
    def Get_Email():
        return parser.get("Env Details", "UserEmail")

    @staticmethod
    def Get_Pwd():
        return parser.get("Env Details", "Password")