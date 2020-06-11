import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

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
   # print('predicted response:', y_pred, sep='\n')
    
    x_new = np.arange(5).reshape((-1, 1))
    #print(x_new)
    
    y_new = model.predict(x_new)
   # print(y_new)
    
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
    
   
def graphScatter(x, y, pName, pFig:int, pColor: str):
    #plt.figure(pFig)
    plt.scatter(x, y, label= "stars", color= pColor,  
            marker= "*")
    xStr = str(x)
    yStr = str(y)
    dataController = DataController("./data/data_saver")
    dataController.writeToFile(xStr, "x_data_" + pName + ".json")
    dataController.writeToFile(yStr,  "y_data_" + pName + ".json")

    
    # naming the x axis 
    plt.xlabel('temperature - axis') 
    # naming the y axis 
    plt.ylabel('humidity - axis') 
      
    # giving a title to my graph 
    plt.title(pName) 
      
    # function to show the plot 
    #plt.show()
    
def graphLine(x, y, pName, pFig:int, pColor: str):
    #plt.figure(pFig)
    plt.plot(x, y, label= "dots", color= pColor)
    
    xStr = str(x)
    yStr = str(y)
    dataController = DataController("./data/data_saver")
    dataController.writeToFile(xStr, "x_data_" + pName + ".json")
    dataController.writeToFile(yStr,  "y_data_" + pName + ".json")

    # naming the x axis 
    plt.xlabel('temperature - axis') 
    # naming the y axis 
    plt.ylabel('humidity - axis') 
      
    # giving a title to my graph 
    plt.title(pName) 
      
    # function to show the plot 
    #plt.show() 



def temp_humidity_lr(pHostUserName, pFigNum):
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
    #print('predicted response:', humidity_pred, sep='\n')
    time.sleep(1)
    predictedName = pHostUserName + " - Predicted humidity values from Linear Regression based on orignal temperature values"
    plt.figure(pFigNum)
    pFigNum = pFigNum + 1
    graphLine(temperature, humidity_pred, predictedName, pFigNum, "blue")
    time.sleep(1)
    dataName = pHostUserName + " - Orignal recorded datapoint values"
    graphScatter(temperature, humidity, dataName, pFigNum, "green")
    #time.sleep(1)
    
    temperature_new = np.arange(5, 45, 0.05).reshape((-1, 1))
    
    humidity_new = model.predict(temperature_new)
    #print(humidity_new)
    newName = hostUserName + " - Predicied humidity values from Linear Regression"
    graphLine(temperature_new, humidity_new, newName, pFigNum, "pink")

    return temperature, humidity, pFigNum

def temp_humidity_polynom_regression(pHostUserName, pFigNum):
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
    #print("----- Polynomial Transformed X values ------")
   # print(temperature_)
    
    
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
  #  print('predicted response:', humidity_pred, sep='\n')
    polyGraphName = pHostUserName + " - Polynomial prediction - Temperature and humidity"
    plt.figure(pFigNum)
    pFigNum = 1 + pFigNum
    graphLine(temperature_[:, 0], humidity_pred, polyGraphName, pFigNum, "blue")
    #graphScatter(temperature_[:, 0], humidity_pred, polyGraphName, pFigNum, "green")
    orignalDataPolyName = pHostUserName + " - Polynomial orignal data - Temperature and humidity"
    graphScatter(temperature, humidity, orignalDataPolyName, pFigNum, "pink")
    newName = hostUserName + "Prediciedt humidity values from Linear Regression"

    #40/0.05 = 800 which is same number of datpoints being analysed
   # temperature_new = np.arange(5, 45, 0.05).reshape((-1, 1))    
   #humidity_new = model.predict(temperature_new)
    #print(humidity_new)
    
    return temperature, humidity, pFigNum

def variance(data_type: str, lukeDataArray, joshDataArray):
    variance_luke =  lukeDataArray.var()
    print("-----------" + data_type + "variance of Lukes data --------------------" )
    print(variance_luke)
    
    variance_josh =  joshDataArray.var()
    print("-----------" + data_type + "variance of Josh' data --------------------" )
    print(variance_josh)
    
def variance_between_data_sets(lukeDataArray, joshDataArray):
    variance_array = []
    arrayLength = len(lukeDataArray)
    for i in range(arrayLength):
        tempVarianceArray = np.array([lukeDataArray[i], joshDataArray[i]])
        new_variance =  tempVarianceArray.var()
        #            varianceArray.append(lukeDataArray[i], joshDataArray[i])
        variance_array.append(new_variance)
    return variance_array
        
def plot_variance(variance_array, pFigNum):
    plt.figure(pFigNum)
    dataPointArray = []
    for i in range(len(variance_array)):
        dataPointArray.append(i)
    graphName = "Variance between each datapoint of both temperature sensor values"
    graphLine(dataPointArray, variance_array, graphName, pFigNum, "blue")

def plot_original_data_with_mean(arr1, arr2, pFigNum):
    plt.figure(pFigNum)
    #arr1.mean()
    graphName = "Scatter plot of temperature from both sensors"
   # graphLine(dataPointArray, variance_array, graphName, pFigNum, "blue")
    graphName = "Variance between each datapoint of both temperature sensor values"
    #graphLine(dataPointArray, variance_array, graphName, pFigNum, "blue")


def standard_deviation(data_type: str, lukeDataArray, joshDataArray):
    variance_luke =  lukeDataArray.std()
    print("=================" + data_type + "Standard Deviation  of Lukes data =================" )
    print(variance_luke)
    
    variance_josh =  joshDataArray.std()
    print("=================" + data_type + "Standard Deviation  of Josh' data =================" )
    print(variance_josh)


if __name__ == "__main__":
    #tutorial()
    #plt_test()
    ### Use th enext twoi lines to update files from online database
    #update_data_from_server("luke")
   # update_data_from_server("josh")
   
    hostUserName = "luke"
    startingFigNumber = 1
    temperature_luke, humidity_luke, startingFigNumber = temp_humidity_lr(hostUserName, startingFigNumber)
    temperature_luke, humidity_luke, startingFigNumber = temp_humidity_polynom_regression(hostUserName, startingFigNumber)
    
    hostUserName = "josh"
    temperature_josh, humidity_josh, startingFigNumber = temp_humidity_lr(hostUserName, startingFigNumber)
    temperature_josh, humidity_josh, startingFigNumber = temp_humidity_polynom_regression(hostUserName, startingFigNumber)

    variance("Temperature: ", temperature_luke, temperature_josh)
    variance("Humidity: ", humidity_luke, humidity_josh)
    new_variance_array = variance_between_data_sets(temperature_luke, temperature_josh)
   # startingFigNumber = startingFigNumber + 1
    plot_variance(new_variance_array, startingFigNumber)
    startingFigNumber = startingFigNumber + 1
    
    standard_deviation("Temperature: ", temperature_luke, temperature_josh)
    standard_deviation("Humidity: ", humidity_luke, humidity_josh)

    plt.show()
    

