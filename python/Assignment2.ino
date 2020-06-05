#include "DHT.h"
#include "LiquidCrystal.h"
#include <ArduinoJson.h>
#include <Time.h>
unsigned long clocktime;




#define DHTPIN A5     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT 11

DHT dht(DHTPIN, DHTTYPE);
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
StaticJsonDocument<200> json_data;

String stringData;
int incomingByte = 0; // for incoming serial data

void setup() {  
  Serial.begin(115200);
  dht.begin();
}

void loop() {  
  stringData = "";
  lcd.clear();

  float h = dht.readHumidity();
  float t = dht.readTemperature();

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);
  String lcd_temp = String(h) + "%    " + String(hic) + "C";
  lcd.print(lcd_temp);

  json_data["temp"] = hic;
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

  if (stringData.length() > 0){
    lcd.print(stringData);
    delay(3000);
  } 
}
