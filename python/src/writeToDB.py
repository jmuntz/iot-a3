
import MySQLdb


def writeToDB(pTemp, pIsHot, pMotorPos):
    dbConn = MySQLdb.connect("localhost", "root", "password", "tempdb") or die("Could not connect to the database")

    print(dbConn)

    #with dbConn:
    try: 
        cursor = dbConn.cursor()
        cursor.execute("INSERT INTO motorTempLog (temp,pos,isHot) VALUES (%s, %s, %s)" % (pTemp, pMotorPos, pIsHot))
    except (MySQLdb.Error) as e:
        print(e)
        dbConn.rollback()
    else:
        dbConn.commit()
    finally:
        cursor.close()
    
