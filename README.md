# Just another IoT project

Root URL for project: 
https://iot.porky.dev/ass3/app

The API is stored under /api:
eg; https://iot.porky.dev/ass3/app/api

All data sent and received should be JSON compliant.

The following endpoints can be used to access or submit data.

**Examples**
* eg; [Temperature and humidity](https://iot.porky.dev/ass3/app/api/get)
* eg; [Devices that have sent data](https://iot.porky.dev/ass3/app/api/get/hosts) 

### GET - fetch data
$ means substitute a variable
```php
integer $limit //limits the number of results. default = 25
string $host //provide the IP of a client computer (aka your public IP) to fetch only results from that PC (IoT device) 

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
```php
// POST data must be an array with three values [string(your IP), string(epoch timestamp), int(value)].
// eg; $arr = ["121.241.64.23", "1590993444", 24]

/api/save/temperature
/api/save/humidity
```

### DELETE - delete yo datas
``` /delete [not yet implemented] ```


