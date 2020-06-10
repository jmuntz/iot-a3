import requests, json
import urllib.request, urllib.parse
from urllib import request, parse
import random
import time

class DataController:
        
    def __init__(self):      
        self.__url = "http://iot.porky.dev/ass3/app/api"
        self.__host = "/144.136.177.59"
        
        
    def get_sample(self):
        url = "http://iot.porky.dev/ass3/app/api/get/temperature/5"

        #randnum = random.randint(10,26)

        contents = urllib.request.urlopen(url).read()

        r = requests.get(url)
        req = urllib.request.Request(url)
        parsed = urllib.request.urlopen(req).read()
        cont = json.loads(parsed.decode('utf-8'))
        #contents_string = json.dump(cont)
        
        print(cont)
        
    def get_contents_of_url(self, urlString):
        url = self.__url + urlString
        print(url)
        
        contents = urllib.request.urlopen(url).read()
        
        return contents
    
    def save_url_contents_to_file(self, urlString:str, pFileSource: str):
        file_object = open(pFileSource, "w+")
        contents = str(self.get_contents_of_url(urlString))
        file_object.write(contents)
    
    def get_request(self, pString):
        url_request = self.__url + "/get" + pString
        print(url_request)
        r = requests.get(url_request)
        req = urllib.request.Request(url_request)
        parsed = urllib.request.urlopen(req).read()
        cont = json.loads(parsed.decode('utf-8'))
        contents_string = json.dumps(cont)

        print(contents_string)
        return contents_string
        
    def get_temperature_limit(self, pLimit: int):
        string_req = "/temperature/" + str(pLimit) + self.__host
        print(string_req)
        temperatureData = str(self.get_request(string_req))
       # temperatureData = """"temperature":""" + temperatureData
        print("---------received online temperature")
        print(temperatureData)
        print("---------")
        return temperatureData
     
    def get_humidity_limit(self, pLimit: int):
        string_req = "/humidity/" + str(pLimit) + self.__host
        #print(string_req)
        #print("---------")
        humidityData = str(self.get_request(string_req))
        #humidityData = """"humidity":""" + humidityData
        print("---------received online humidity")
        print(humidityData)
        print("---------")
        return humidityData
    
    def get_temp_humidity_limit(self, pLimit):
        string_req = "/humidity/" + str(pLimit)
        print(string_req)
        get_request(string_req)
        
    def writeToFile(self, pContents, pFileSource):
        file_object = open(pFileSource, "w+")
        file_object.write(pContents)
    
    
    def convert_temp_data_intoArray():
        latest_temp_id = 4
        latest_humidity_id = 5
        #from x in range(latest_temp_id)  

if __name__ == "__main__":
    dataController = DataController()
    
    #dataController.get_sample()
    #time.sleep(4)
    humidity = dataController.get_humidity_limit(800)
    time.sleep(5)
    dataController.writeToFile(humidity, "humidity.json")
    temperature = dataController.get_temperature_limit(800)
    time.sleep(4)
    dataController.writeToFile(temperature, "temperature.json")
  
    #time.sleep(6)
#    dataController.save_url_contents_to_file("/get/temperature/1000/144.136.177.59", "data.json")

    
    