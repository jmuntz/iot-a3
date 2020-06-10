import json
import sys
sys.path.insert(1, '../playground')

class JsonDataProcessor:
    
    data = "{'temp':0.0,'humidity':0.0}"

    
    def __init__(self):
        self.__data = {"temp":0.0,"humidity":0.0}
        self.__json_string = json.dumps(self.__data)
        self.__json_dictionary = json.loads(self.__json_string)
        self.__json_databytes = self.__json_string.encode('utf-8')
        print("Serial data: " + self.__json_string)
        
        self.__temperature = 0
        self.__humidity = 0
        self.__motorPos = 0
        self.__fanOn = 0
        # self.updateDataToProcess(pData)
        # self.move_servo(servo_position)
       
    def append_actuator_data_to_json(self, pMotorPos: float, pFanIsOn: int):
        dc_motor_data = {"fanIsOn": pFanIsOn}
        # python object to be appended 
        servo_data = {"motorPos": pMotorPos} 
          
        # parsing JSON string to dictionary: 
        self.__json_dictionary = json.loads(self.__data) 
        
        # appending the data 
        self.__json_dictionary.update(servo_data)
        self.__json_dictionary.update(dc_motor_data)
        self.set_json_string(self.__json_dictionary)
        # the result is a JSON string: 
        print(json.dumps(self.__json_dictionary))
        
    def key_exists(self, pKey):
        if (pKey != "motorPos" and pKey != "fanIsOn"):
            print("Key not recognised")
            return False
        if(pKey == "motorPos"):
            print("key recognised")
            if (pKey in self.__json_dictionary):
                print("motorPos data has been appended!")
                return True
            else:
                print("motorPos has not yet been appended")
                return False
        elif(pKey == "fanIsOn"):
            print("key recognised")
            if(pKey in self.__json_dictionary):
                print("fanIsOn data has been appended!")
                return True
            else:
                print("fanIsOn has not yet been appended")
                return False
        else:
            print("!!!!! Key not recognised. ERROR: Unexpected logic exception bug !!!!!")
            return False
    
    def motor_data_validator(self):
        if(self.__motorPos <= -1):
            self.__motorPos = -1
        elif(self.__motorPos >= 1):
            self.__motorPos = 1

    def update_DataToProcess(self, pData):
        self.__data = pData
        self.set_json_dictionary(pData)
        #self.__json_dictionary(self.__data)
        #print(pData)
        #print(self.__json_dictionary)
        self.set_json_string(self.__json_dictionary)
        self.set_json_databytes(self.set_json_string)
        self.set_temperature(self.__json_dictionary["temp"])
        self.__humidity = self.__json_dictionary["humidity"]
        
        # if key exists then update the values of respective key. Else leave it alone

        #print(self.__json_dictionary)
        #print(self.__json_string)
        return self.__json_dictionary
        
    def convert_temp_data_into_Array(self, data):
        print("-----------------OLD CODE: Converting json data to array---------------")
        #get max id in json object
        #event = max(data['id'])
        event = max(data, key=lambda ev: ev['id'])
        print(event)
        #latest_temp_id
        #latest_humidity_id
        #from in range(latest_temp_id)
    
    def get_max_id_of_object(self, data):
        event = max(data, key=lambda ev: ev['id'])
        print(event["id"])
    
    def read_json_from_file(self, pDataType):
        print("-----------------Reading JSON File---------------")
        with open("/home/pi/Desktop/iot-a3/python/playground/" + pDataType + ".json") as json_file:
            print(json_file)
            data = json.load(json_file)
            print(data)
            return data
        
    def convert_jsonfile_to_array(self, pDataType):
        array = []
        #print("-----------------Converting JSON objects into Array---------------")
        with open("/home/pi/Desktop/iot-a3/python/playground/" + pDataType + ".json") as json_file:
             for jsonObj in json_file:
                dataPoint = json.loads(jsonObj)
                array.append(dataPoint)
        #print(array)
        dataArray = []
        print("--------------Getting " + pDataType + " values from each JSON Decoded Object in JSON File--------------")
        for actualArray in array:
            dataArray = actualArray
        valueArray = []
        for data in dataArray:
            #print(data["id"], data["client_addr"], data["timestamp"], data["value"])
            valueArray.append(int(data["value"]))
        #for value in valueArray:
            #print(value)
        
        return valueArray
    
    
        
    
    ### Getters and Setters ###    
    def set_data(self, pData):
        self.__data = pData
    
    def get_data(self): 
        self.__data = self.data
        return self.data
   
    def set_json_dictionary(self, json_string): 
        self.__json_dictionary = json.loads(json_string)    
       ### Same as?: self.__json_dictionary = json.loads(self.__data)???    

    def get_json_dictionary(self): 
        return self.__json_dictionary   
    
    def set_json_string(self, data): 
        self.__json_string = json.dumps(data)    
       
    def get_json_string(self): 
        return self.__json_string
    
    def set_json_databytes(self,pString):
        self.__jsondataasbytes = self.__json_string.encode('utf-8')
    
    def get_json_databytes(self):
        return self.__jsondataasbytes
    
    def set_temperature(self, temperature): 
        self.__temperature = temperature
         
    def get_temperature(self): 
        return self.__temperature

    def set_humidity(self, humidity): 
        self.__humidity = humidity
        
    def get_humidity(self): 
        return self.__humidity
     
    def set_motorPos(self, motorPos): 
        self.__motorPos = motorPos
     
    def get_motorPos(self): 
        return self.__motorPos
    
    def set_fanIsOn(self, fanIsOn):
        self.__fanIsOn = fanIsOn

    def get_fanIsOn(self):
        return self.__fanIsOn

if __name__ == '__main__':
    json_processor = JsonDataProcessor()
    json_processor.update_DataToProcess("""{"temp":5.0,"humidity":40.0}""")
    #json_processor.append_actuator_data_to_json(200, True)
    #json_processor.key_exists("motorPos")
    data = json_processor.read_json_from_file("humidity")
    dataArray = json_processor.convert_jsonfile_to_array("humidity")
    json_processor.get_max_id_of_object(data)
#    json_processor.key_exists("fanIsOn")
    
