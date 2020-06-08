#include "DHT.h"
#include <ArduinoJson.h>
//#include <Time.h>
unsigned long clocktime;




#define DHTPIN 2     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT 11

DHT dht(DHTPIN, DHTTYPE);
StaticJsonDocument<200> json_data;

String stringData;
int incomingByte = 0; // for incoming serial data

void setup() {  
  Serial.begin(115200);
  dht.begin();
}

void loop() {  
  stringData = "";


  float h = dht.readHumidity();
  float t = dht.readTemperature();

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  json_data["temp"] = t;
  json_data["humidity"] = h;
  
  
  if (!Serial.available()) {
    serializeJson(json_data, Serial); 
    delay(5000); 
    return;
  } else {
     while (Serial.available()) {
        if (Serial.available() > 0) {
          char c = Serial.read();  //gets one byte from serial buffer
          stringData += c; //makes the string readString
        } 
        else break;   
    } 
  }
}


