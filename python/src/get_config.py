import requests, json
import urllib.request, urllib.parse
from urllib import request, parse
import time

class PhysicalSystemConfiguration:


    def get_config(self):
        url = "http://iot.porky.dev/ass3/app/api/get/config"

        contents = urllib.request.urlopen(url).read()
        time.sleep(10)
        r = requests.get(url)
        req = urllib.request.Request(url)
        time.sleep(10)
        parsed = urllib.request.urlopen(req).read()
        self.__config = json.loads(parsed.decode('utf-8'))
        
        print(self.__config)
        return self.__config

    def process_dictionary_to_string(self):
        json_string = json.dump(self.__config)
        return json_string

    def extract_motorPos(self):
        return self.__config["motorPosition"]

    def extract_fanIsOn(self):
        return self.__config["fanSpeed"]

    def extract_status(self):
        if ("status" in self.__config):
            return self.__config["status"]
        else:
            return "OFF"

if __name__ == "__main__":
    sysConfig = PhysicalSystemConfiguration()
    config = sysConfig.get_config()
    print(sysConfig.extract_motorPos())
    print(sysConfig.extract_fanIsOn())
    print(sysConfig.extract_status())

