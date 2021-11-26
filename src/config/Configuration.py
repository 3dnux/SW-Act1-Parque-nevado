import json
import pathlib
import string


class Configuration:
    file_config = ""

    def __init__(self, environment: string) -> any:
        file_path = pathlib.Path().absolute()
        self.file_config = json.load(
            open(str(file_path) + "/src/config/" + environment + '/configuration' + environment + '.json'))

    def getHostDB(self) -> string:
        return str(self.file_config["db"]["postgresql"]["hostname"])

    def getUserDB(self) -> string:
        return str(self.file_config["db"]["postgresql"]["username"])

    def getPasswordDB(self) -> string:
        return str(self.file_config["db"]["postgresql"]["password"])

    def getDatabaseDB(self) -> string:
        return str(self.file_config["db"]["postgresql"]["database"])

    def getPortDB(self) -> string:
        return str(self.file_config["db"]["postgresql"]["port"])
