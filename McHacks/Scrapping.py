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

    def ScrapValue(self,filename,countColCountry,countColValue):
        tableStats = self.soup.findAll("table", attrs={'class': "sortable wikitable"})

        #fo = open(filename + ".txt", "w")
        dictValueForCountry = {}
        for myTableStats in tableStats:
                trStats = myTableStats.find_all("tr")

                for myTrStats in trStats:
                    tdStats = myTrStats.find_all("td")
                    countColNumber=0
                    vCountry = None
                    vValue= None
                    vValidLine =True

                    for myTdStats in tdStats:

                        if vValidLine:
                            if countColNumber == countColCountry:
                                aStats = myTdStats.find_all("a")
                                if aStats:

                                    for myAStats in aStats:
                                        country = myAStats.get("title") # This shows only the countries with titles
                                        if country:
                                            # fo.write(v)
                                            #print("true")
                                            print(country)
                                            vCountry=country
                                        else:
                                            #print("false")
                                            vValidLine=False
                                else:
                                    #print("false")
                                    vValidLine=False
                            elif(countColNumber==countColValue):

                                myTdStats = str(myTdStats)
                                start = myTdStats.index(">") + 1
                                end = myTdStats[start:].index("<")
                                tdValue = myTdStats[start:(start + end)]
                                if (tdValue):
                                    #print(tdValue)
                                    vValue=tdValue
                                else:
                                    #print("None")
                                    vValue=None

                        else:
                            break
                        countColNumber += 1
                    if vValidLine :
                        dictValueForCountry[vCountry]=vValue


        #fo.close()
        print(dictValueForCountry)
        return dictValueForCountry

    def BirthRate(self):
        url = "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_birth_rate"
        self.OpenURL(url)
        self.ScrapValue("BirthRate",0,7)

    def DeathRate(self):
        url = "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_mortality_rate"
        self.OpenURL(url)
        self.ScrapValue("DeathRate")


