import serial
import io
import MySQLdb

#Make DB connection

dbConn = MySQLdb.connect("43.250.140.18", "porkydev_iot_ass3", "LptWXCLR;$k;", "porkydev_iot_ass3") or die("Could not connect to the database")

print(dbConn)

#with dbConn:
try: 
    cursor = dbConn.cursor()
    #cursor.execute("INSERT INTO tempLog (Temperature) VALUES (%s)" % (temp))
except (MySQLdb.Error) as e:
    print(e)
    dbConn.rollback()
else:
    dbConn.commit()
finally:
    cursor.close()
