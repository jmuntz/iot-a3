import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import PolynomialFeatures

import time
# importing the required module 
import matplotlib.pyplot as plt 

import sys
sys.path.insert(1, '../src')
from json_data_processor import JsonDataProcessor
from get_data import DataController

from random import randrange


def tutorial_lr():
    
    # -----------------------data collection processing -----------------------
    x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
    y = np.array([5, 20, 14, 32, 22, 38])
    
    print(x)
    print(y)
    
    # -----------------------data collection processing -----------------------
    model = LinearRegression()

    #calcu-latte(ha-ha) optimum weights
    model.fit(x, y)
    
    #SHORTCUT:does two lines above at once
    #model = LinearRegression.fit(x, y)
    
    
#def get_results():
    #score are predictor x and regressor y
    r_sq = model.score(x, y)
    print('coefficient of determinaltion: ', r_sq)
    
    print('intercept:', model.intercept_)
    
    print('slope:', model.coef_)

    ### give y as a two dimensional array to see if results change
    new_model = LinearRegression().fit(x, y.reshape((-1, 1)))
    print('intercept:', new_model.intercept_)
    print('slope:', new_model.coef_)
    
    ###Predict results( this will also be in a function below get_results()
    y_pred = model.predict(x)
    print('predicted response:', y_pred, sep='\n')
    
    x_new = np.arange(5).reshape((-1, 1))
    print(x_new)
    
    y_new = model.predict(x_new)
    print(y_new)
    
def get_data_from_json(pfileHostName):
    data_controller = DataController(pfileHostName)
    userName = data_controller.get_name()
    json_processor = JsonDataProcessor()
    #data collection
    temperatureArray = json_processor.convert_jsonfile_to_array(userName, "temperature")
    humidityArray = json_processor.convert_jsonfile_to_array(userName, "humidity")
    #print("##Size of Temperature Array: " + str(len(temperatureArray)))
    #print("##Size of Humidity Array: " + str(len(humidityArray)))
    return temperatureArray, humidityArray
   
def update_data_from_server(pfileHostName):
    data_controller = DataController(pfileHostName)
    
    humidity = data_controller.get_humidity_limit(800)
    time.sleep(5)
    data_controller.writeToFile(humidity, "humidity.json")
    temperature = data_controller.get_temperature_limit(800)
    time.sleep(4)
    data_controller.writeToFile(temperature, "temperature.json")
    
   
def graphScatter(x, y, pName, pFig:int):
    #plt.figure(pFig)
    plt.scatter(x, y, label= "stars", color= "green",  
            marker= "*", s=30) 
    
    # naming the x axis 
    plt.xlabel('temperature - axis') 
    # naming the y axis 
    plt.ylabel('humidity - axis') 
      
    # giving a title to my graph 
    plt.title(pName) 
      
    # function to show the plot 
    #plt.show()
    
def graphLine(x, y, pName, pFig:int):
    plt.figure(pFig)
    plt.plot(x, y, label= "dots", color= "blue")
    
    # naming the x axis 
    plt.xlabel('temperature - axis') 
    # naming the y axis 
    plt.ylabel('humidity - axis') 
      
    # giving a title to my graph 
    plt.title(pName) 
      
    # function to show the plot 
    #plt.show() 

def temp_humidity_lr(pHostUserName):
    #json_processor = JsonDataProcessor()
    #data collection
    #temperatureArray = json_processor.convert_jsonfile_to_array("temperature")
    #humidtyArray = json_processor.convert_jsonfile_to_array("humidity")
    temperatureArray, humidtyArray = get_data_from_json(pHostUserName)
    
    #data processing: Temp(predictor) is independant and humidity(regressor) is dependant on temperature
    temperature = np.array(temperatureArray).reshape((-1, 1))
    humidity = np.array(humidtyArray)

    #print(temperature)
   #print(humidity)
    
    # -----------------------modelling data from Linear Regression model -----------------------
    model = LinearRegression()

    #calcu-latte(ha-ha) optimum weights
    model.fit(temperature, humidity)
    
    #score are predictor x and regressor y
    r_sq = model.score(temperature, humidity)
    print('coefficient of determinaltion: ', r_sq)
    
    print('intercept:', model.intercept_)
    
    print('slope:', model.coef_)
    
    ###Predict results( this will also be in a function below get_results()
    humidity_pred = model.predict(temperature)
    print('predicted response:', humidity_pred, sep='\n')
    time.sleep(1)
    predictedName = hostUserName + " - Predicted humidity values from Linear Regression based on orignal temperature values"
    graphLine(temperature, humidity_pred, predictedName, 2)
    time.sleep(1)
    predictedName = hostUserName + " - Orignal recorded datapoint values"
    graphScatter(temperature, humidity, dataName, 3)
    #time.sleep(1)
    
    temperature_new = np.arange(5, 45, 0.05).reshape((-1, 1))
    print(temperature_new)
    
    humidity_new = model.predict(temperature_new)
    #print(humidity_new)
    newName = hostUserName + " - Predicied humidity values from Linear Regression"
    graphLine(temperature_new, humidity_new, newName, 2)

    return temperature_new, humidity_new

def temp_humidity_polynom_regression(pHostUserName):
    temperatureArray, humidtyArray = get_data_from_json(pHostUserName)
    
    #data processing: Temp(predictor) is independant and humidity(regressor) is dependant on temperature
    temperature = np.array(temperatureArray).reshape((-1, 1))
    humidity = np.array(humidtyArray)

    #print(temperature)
    #print(humidity)

    ###-----------------------polynomial feature transformation -----------------------###
    #interactio paramater is false by defult. Will include only interactive features
    #incelude_bias chooses whether or not to include intercept column 
    transformer = PolynomialFeatures(degree=2, include_bias=False)
    #fit transformer with independant variable
    transformer.fit(temperature)
    # new modified input
    temperature_ = transformer.transform(temperature)
    print("----- Polynomial Transformed X values ------")
    print(temperature_)
    
    
    ### -----------------------modelling data from Linear Regression model -----------------------###
    model = LinearRegression()

    #calcu-latte(ha-ha) optimum weights
    model.fit(temperature_, humidity)
    
    #score are predictor x and regressor y
    r_sq = model.score(temperature_, humidity)
    print('coefficient of determinaltion: ', r_sq)
    
    print('intercept:', model.intercept_)
    
    print('slope:', model.coef_)
    
    ###Predict results( this will also be in a function below get_results()
    humidity_pred = model.predict(temperature_)
    print('predicted response:', humidity_pred, sep='\n')
    polyGraphName = "Polynomial prediction - Temperature and humidity" 
    graphLine(temperature_, humidity_pred, polyGraphName, 1)
    graphScatter(temperature, humidity, polyGraphName, 1)
    newName = hostUserName + "Prediciedt humidity values from Linear Regression"

    #40/0.05 = 800 which is same number of datpoints being analysed
    temperature_new = np.arange(5, 45, 0.05).reshape((-1, 1))
    print(temperature_new)
    
    humidity_new = model.predict(temperature_new)
    #print(humidity_new)
    
    return temperature_new, humidity_new

def predict_response(model): 
    y_pred = model.predict(x)
    print('predicted response:', y_pred, sep='\n')

if __name__ == "__main__":
    #tutorial()
    #plt_test()
    #update_data_from_server("luke")
    arrayDatax = []
    arrayDatay = []
    for i in range(800):
        arrayDatax.append(randrange(5, 45))
        arrayDatay.append(randrange(90))
        
   # hostUserName = "luke"
    tempearature_new, humidity_new = temp_humidity_lr(hostUserName)
    #newName = hostUserName + "Prediciedt humidity values from Linear Regression"
    # actual temp and humidity data aobservvations
    #temperature_data, humidity_data = get_data_from_json(hostUserName)
   # print("##Size of Temperature Array: " + str(len(temperature_data)))
   # print("##Size of Humidity Array: " + str(len(humidity_data)))
    
   # dataName = hostUserName + "recorded data values"
    #plt_tutorial()
    
  #  graphLine(tempearature_new, humidity_new, newName, 2)
   # time.sleep(1)
   # graphScatter(temperature_data, humidity_data, dataName, 3)
   # time.sleep(1)
    
    hostUserName = "josh"
    #tempearature_new, humidity_new = temp_humidity_lr(hostUserName)
    #newName = hostUserName + "Prediciedt humidity values from Linear Regression"
    # actual temp and humidity data aobservvations
    #temperature_data, humidity_data = get_data_from_json(hostUserName)
    
    #dataName = hostUserName + "recorded data values"
    #plt_tutorial()
   # print("##Size of Temperature Array: " + str(len(temperature_data)))
   # print("##Size of Humidity Array: " + str(len(humidity_data)))
    
    #graphLine(tempearature_new, humidity_new, newName, 4)
   # time.sleep(1)
   # graphScatter(temperature_data, humidity_data, dataName, 5)
    #time.sleep(1)
    #graphScatter(arrayDatax, arrayDatay, "testData", 6)
    time.sleep(1)
    plt.show()
    

