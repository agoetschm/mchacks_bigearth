import urllib.request
from bs4 import BeautifulSoup

class Scrapping:
    def __init__(self):
        self.soup =None

    def OpenURL(self,url):
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        open = urllib.request.urlopen(req)
        readHtml = open.read()
        self.soup = BeautifulSoup(readHtml, "html.parser")

    def ScrapValue(self,filename):
        tableStats = self.soup.findAll("table", attrs={'class': "sortable wikitable"})

        fo = open(filename + ".txt", "w")

        for myTableStats in tableStats:
            #tbodyStats = myTableStats.find_all("tbody")
            #for myTbodyStats in tableStats:
                trStats = myTableStats.find_all("tr")
                for myTrStats in trStats:
                    tdStats = myTrStats.find_all("td")
                    for myTdStats in tdStats:
                        aStats = myTdStats.find_all("a")
                        for myAStats in aStats:
                            val = []
                            val.append(myAStats.get("title"))
                            val = list(filter((None).__ne__, val))
                            for v in val:
                                fo.write(v)
                                #print(v)

                        myTdStats = str(myTdStats)
                        start = myTdStats.index(">") + 1
                        end = myTdStats[start:].index("<")
                        if myTdStats[start:(start + end)] != '0':
                            #print(myTdStats[start:(start + end)])
                            fo.write(myTdStats[start:(start + end)] + "\n");
                        else:
                            continue
        fo.close()

    def BirthRate(self):
        url = "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_birth_rate"
        self.OpenURL(url)
        self.ScrapValue("BirthRate")

    def DeathRate(self):
        url = "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_mortality_rate"
        self.OpenURL(url)
        self.ScrapValue("DeathRate")


