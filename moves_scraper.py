from bs4 import BeautifulSoup
import urllib.request
import csv

class Scraper:
    
    def Scrape(self):
        #Get the url and then read the data on that url
        baseurl = "http://pokemondb.net/move/generation/1"
        url = urllib.request.urlopen(baseurl).read()

        #pass the data to a beautiful soup object
        soup = BeautifulSoup(url)

        tables = soup.find_all("table", attrs={"class": "data-table wide-table"})
        names = soup.find_all("a", attrs={"class": "ent-name"})
        types = soup.find_all("a", attrs={"class": "type-icon"})
        pp = soup.find_all("td", attrs={"class": "num"})
        effects = soup.find_all("td", attrs={"class": "long-text"})

        with open("Moves.csv", "w", newline = '') as csvfile:
            outwriter = csv.writer(csvfile)
            counter = 0
            for name in names:
                move = name.get_text()
                move_type = types[counter].get_text()
                points = pp[((counter + 1)*3)-1].get_text()
                effect = effects[counter].get_text()
                counter += 1
                outwriter.writerow([move] + [move_type] + [points] + [effect])
        #find the correct table and its descendants
       # tables = soup.find_all("table", attrs={"class": "wsod_dataTable wsod_dataTableBig"})
        #symbols = soup.find_all("a", attrs={"class": "wsod_symbol"})
        #children = tables[0].find_all("td", attrs={"class": "wsod_aRight"})

        #open the output file and write the data from the table to the file
        #with open("Scraper_Output.csv", "w", newline = '') as csvfile:
         #   outputwriter = csv.writer(csvfile)
          #  counter = 0
           # for symbol in symbols:
            #    if any(symbol):
             #       if "symb" in str(symbol.get('href')):
              #          ticker = symbol.contents[0]
               #         price = children[counter].get_text()
                #        counter += 1
                 #       change = children[counter].get_text()
                  ##     outputwriter.writerow([ticker] + [price] + [change])
                    #    counter += 2


X = Scraper()
X.Scrape()
