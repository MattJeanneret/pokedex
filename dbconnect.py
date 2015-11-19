import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(host='',
                                    user='',
                                    database='pokedex',
                                    password='')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = cnx.cursor()
    cursor.close
    cnx.close
