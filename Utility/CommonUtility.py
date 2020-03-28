import json
import sys
import traceback
sys.path.append("../")

class commonUtility(object):

    @staticmethod
    def parse_JSON_file(jsonFilePath):
        try:
            parsed_json = json.load(open(jsonFilePath))
            return parsed_json
        except Exception:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)

    @staticmethod
    def read_config_file():
        try:
            parsed_json = json.load(open("../Config/config.json"))
            return parsed_json
        except Exception:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)

