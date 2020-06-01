# Just another IoT project

Primary domain: 
https://iot.porky.dev/ass3/app

The API is accessed from /api:
https://iot.porky.dev/ass3/app/api

The following endpoints can be used to access or submit data.

### GET - fetch yo datas
$ means substitute a variable
```
integer $limit //limits the number of results
string $host //provide the IP of a client computer (aka your public IP)t o fetch only results from that PC (IoT device) 

/api/get 
/api/get/temperature 
/api/get/temperature/$limit
/api/get/temperature/$limit/$host
/api/get/humidity 
/api/get/humidity/$limit
/api/get/humidity/$limit/$host
/api/get/hosts
```

### SAVE - save yo datas
Request type must be POST when sending your data here from Python/your IOT device.
```
// POST data must be an array with three values [string(your IP), string(epoch timestamp), int(value)].
// eg; $arr = ["121.241.64.23", "1590993444", 24]

/api/save/temperature
/api/save/humidity
```

### DELETE - delete yo datas
``` /delete [not yet implemented] ```
