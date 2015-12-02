import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(host='10.104.251.10',
                                    user='jeanmc12',
                                    database='pokedex',
                                    password='Matt')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = cnx.cursor()
    query = "Select pokemonName, pokemonType1, pokemonType2 from Pokemon"
    cursor.execute(query)
    for(pokemonName, pokemonType1, pokemonType2) in cursor:
        print("{}, {}, {} ".format(pokemonName, pokemonType1, pokemonType2))
    cursor.close
    cnx.close
