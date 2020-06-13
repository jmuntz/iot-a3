# Just another IoT project

Root URL for project: 
https://iot.porky.dev/ass3/app

The API is stored under /api:
https://iot.porky.dev/ass3/app/api

Create your MySQL databse with the [database_setup.sql](https://github.com/jmuntz/iot-a3/blob/master/database_setup.sql) script.

Save your DB credentials in /config.php. 

All data sent and received should be JSON compliant.

The following endpoints can be used to access or submit data.

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
/api/get/config
```

**Examples**
* eg; [Temperature and humidity - /api/get](https://iot.porky.dev/ass3/app/api/get)
* eg; [Devices that have sent data - /api/get/hosts](https://iot.porky.dev/ass3/app/api/get/hosts) 

### SAVE - save data
Request type must be POST when sending your data here from Python/your IoT device.
If you simply go to these URL's in your browser (AKA GET request) you will get a 404 error.

Data sent should be a simple array and sent to the endpoint that you wish to save the data as.
```php

/api/save/temperature
/api/save/humidity
```

### UPDATE - update data
``` /update/config ```
Used to update the config file which is saved as a JSON file on the webserver.


