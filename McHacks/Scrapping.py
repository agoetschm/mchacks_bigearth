import urllib.request
from bs4 import BeautifulSoup

class Scrapping:

    def OpenURL(self,url):
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        open = urllib.request.urlopen(req)
        readHtml = open.read()
        return BeautifulSoup(readHtml, "html.parser")

    def getScrappedFeature(self,url,index,countColCountry,countColValue,year):
        print(url)

        soup = self.OpenURL(url)
        tableStats = soup.findAll("table", attrs={'class': "wikitable"})

        #fo = open(filename + ".txt", "w")
        dictValueForCountry = {}
        myTableStats = tableStats[index]
        #for myTableStats in tableStats:
        trStats = myTableStats.find_all("tr")

        for myTrStats in trStats:
            tdStats = myTrStats.find_all("td")
            countColNumber=0
            vCountry = None
            vValue= None
            hasLink =False
            hasCountry =False

            for myTdStats in tdStats:

                if not hasLink or hasCountry:
                    if countColNumber == countColCountry:
                        aStats = myTdStats.find_all("a")
                        if aStats:
                            hasLink = True
                            #print(aStats)
                            myAStats = aStats[0]
                            #for myAStats in aStats:
                            country = myAStats.get("title") # This shows only the countries with titles
                            if country:
                                # fo.write(v)
                                #print("true")
                                #print(country)
                                vCountry=country
                                hasCountry = True
                            else:
                                pass
                                #print("false")
                        else:
                            pass
                            #print("false")
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
            if hasCountry :
                #print("HEYYYYYYYYYYYYY"+str(vCountry))
                dictValueForCountry[str(vCountry)+"/"+year]=vValue



        #fo.close()
        #print(dictValueForCountry)
        return dictValueForCountry



    def getScrappedData(self):
        params = [["BirthRate","2014","https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_birth_rate",0, 0, 7],
                  ["DeathRate","2014","https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_mortality_rate",0, 0,3],
                  ["FertilityRate","2014","https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_fertility_rate",0, 1,2],
                  ["HappinessRate","2016","https://en.wikipedia.org/wiki/World_Happiness_Report",0, 1,2],
                  ["HDI","2014","https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index",0, 2,3],
                  ["HDI","2014","https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index",1, 2,3],
                  ["HDI","2014","https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index",2, 2,3],
                  ["HDI","2014","https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index",3, 2,3],
                  ["HDI","2014","https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index",4, 2,3],
                  ["HDI","2014","https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index",5, 2,3],
                  ["HDI","2014","https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index",6, 2,3],
                  ["HDI","2014","https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index",7, 2,3]


                  ]

        scrappedData = {}
        scrappedData["labels"] = []

        for label,year,url,index, countryCol, valueCol in params:
            scrappedData["labels"].append(label)
            newFeatureDict = self.getScrappedFeature(url,index,countryCol,valueCol,year)
            for country, feature in newFeatureDict.items():
                if country in scrappedData:
                    scrappedData[country].append(feature)
                else:
                    scrappedData[country] = (len(scrappedData["labels"])-1) * [None] + [feature]



        print(scrappedData)
        return scrappedData



