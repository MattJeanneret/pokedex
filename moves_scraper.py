from bs4 import BeautifulSoup
import urllib.request
import csv

class Scraper:
    
    def Scrape_Moves(self):
        #Get the url and then read the data on that url
        baseurl = "http://pokemondb.net/move/generation/1"
        url = urllib.request.urlopen(baseurl).read()

        #pass the data to a beautiful soup object
        soup = BeautifulSoup(url)

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
                outwriter.writerow([move] + [move_type] + [effect] + [points])

X = Scraper()
X.Scrape_Moves()

