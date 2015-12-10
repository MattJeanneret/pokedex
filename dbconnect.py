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
    inLoop = True
    hashTags = ("#####################################################")
    while(inLoop):
        print("Select which type of query you would like to perform: ")
        print("Enter 1 to view all pokemon and their types")
        print("Enter 2 to view the most expensive item")
        print("Enter 3 to view all Pokemon found on a certain route")
        print("Enter 4 to view all Pokemon and their types who can learn a certain move")
        print("Enter 5 to view all items sold in a certain city")
        print("Enter any other number to exit")
        inputVar = int(input("Please enter your selection:"))
        if inputVar == 1:
            query = "Select pokemonName, pokemonType1, pokemonType2 from Pokemon"
            cursor.execute(query)
            print(hashTags)
            for(pokemonName, pokemonType1, pokemonType2) in cursor:
                print("{}, {}, {} ".format(pokemonName, pokemonType1, pokemonType2))
            print(hashTags)
        elif inputVar == 2:
            query = "Select max(itemPrice) from Items"
            cursor.execute(query)
            print(hashTags)
            for(item) in cursor:
                print(item)
            print(hashTags)
        elif inputVar == 3:
            incInt = int(input("Input a route number: "))
            query = "Select Pokemon.pokemonName from Pokemon inner Join PokemonRoutes on Pokemon.pokemonID = PokemonRoutes.pokemonID where PokemonRoutes.routesID = %s"
            cursor.execute(query, (incInt,))
            print(hashTags)
            for(pokemonName) in cursor:
                print("{} ".format(pokemonName))
            print(hashTags)
        elif inputVar == 4:
            incSTR = str(input("Input a move: "))
            query = ("Select Pokemon.pokemonName, Pokemon.pokemonType1, Pokemon.pokemonType2 from Pokemon join (select Moves.moveName, PokemonMoves.pokemonID from PokemonMoves Join Moves on PokemonMoves.moveID = Moves.moveID) as X on Pokemon.pokemonID = X.pokemonID where X.moveName = %s")
            cursor.execute(query, (incSTR,))
            print(hashTags)
            for (pokemonName, pokemonType1, pokemonType2) in cursor:
                print("{}, {}, {} ".format(pokemonName, pokemonType1, pokemonType2))
            print(hashTags)
        elif inputVar == 5:
            x = 1
            incCity = str(input("Input a city: "))
            query = "select Items.itemName from Items join (select CitiesItems.itemsID, Cities.cityName from CitiesItems join Cities on CitiesItems.citiesID = Cities.citiesID) as X on Items.itemsID = X.itemsID where X.cityName = %s"
            cursor.execute(query, (incCity,))
            print(hashTags)
            for (itemName) in cursor:
                print("{}".format(itemName))
            print(hashTags)
        else:
            print("Exiting")
            inLoop = False;
    cursor.close
    cnx.close
