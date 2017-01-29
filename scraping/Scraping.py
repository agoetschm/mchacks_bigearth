import urllib.request
from bs4 import BeautifulSoup


class Scraping:
    def OpenURL(self, url):
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        open = urllib.request.urlopen(req)
        readHtml = open.read()
        return BeautifulSoup(readHtml, "html.parser")

    def getScrappedFeature(self, url, index, countColCountry, countColValue, year):
        print(url)

        soup = self.OpenURL(url)
        tableStats = soup.findAll("table", attrs={'class': "wikitable"})

        myTableStats = tableStats[index]

        dictValueForCountry = {}

        trStats = myTableStats.find_all("tr")
        for myTrStats in trStats:
            tdStats = myTrStats.find_all("td")
            countColNumber = 0
            vCountry = None
            vValue = None
            hasLink = False
            hasCountry = False

            for myTdStats in tdStats:

                if not hasLink or hasCountry:
                    if countColNumber == countColCountry:
                        aStats = myTdStats.find_all("a")
                        if aStats:
                            hasLink = True
                            # print(aStats)
                            myAStats = aStats[0]
                            # for myAStats in aStats:
                            country = myAStats.get("title")  # This shows only the countries with titles
                            if country:
                                vCountry = country
                                hasCountry = True
                            else:
                                pass
                                # print("false")
                        else:
                            pass
                            # print("false")
                    elif (countColNumber == countColValue):
                        myTdStats = str(myTdStats)
                        start = myTdStats.index(">") + 1
                        end = myTdStats[start:].rindex("<")
                        tdValue = myTdStats[start:(start + end)]
                        if (tdValue):
                            # print(tdValue)
                            vValue = tdValue
                        else:
                            # print("None")
                            vValue = None




                else:
                    break
                countColNumber += 1
            if hasCountry:
                dictValueForCountry[str(vCountry) + "/" + year] = vValue

        return dictValueForCountry

    def getScrappedData(self):
        params = [
            ["BirthRate", "2014",
             "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_birth_rate", 0, 0, 7],
            ["DeathRate", "2014",
             "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_mortality_rate", 0, 0,
             3],
            # ["FertilityRate", "2014",
            #  "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_fertility_rate", 0, 1,
            #  2],
            ["HappinessRate", "2014", "https://en.wikipedia.org/wiki/World_Happiness_Report", 0, 1, 2],# 2016 in fact...
            ["HDI", "2014", "https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index", 0, 2, 3],
            ["HDI", "2014", "https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index", 1, 2, 3],
            ["HDI", "2014", "https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index", 2, 2, 3],
            ["HDI", "2014", "https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index", 3, 2, 3],
            ["HDI", "2014", "https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index", 4, 2, 3],
            ["HDI", "2014", "https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index", 5, 2, 3],
            ["HDI", "2014", "https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index", 6, 2, 3],
            ["HDI", "2014", "https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index", 7, 2, 3],
            ["HomicideRate", "2014", "https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate", 2,
             0, 1],
            # ["LiteracyRate", "2014", "https://en.wikipedia.org/wiki/List_of_countries_by_literacy_rate", 0, 0, 1],# not only 2014
            ["LifeExpectancy", "2014", "https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy", 0, 0, 2],
            # 2015
            ["MedianAge", "2014", "https://en.wikipedia.org/wiki/List_of_countries_by_median_age", 0, 0, 2],  # 2016
            # ["PercentagePoverty", "2014",
            #  "https://en.wikipedia.org/wiki/List_of_countries_by_percentage_of_population_living_in_poverty", 1, 0, 1],
            # diverse years
            ["PopGrowthRate", "2014", "https://en.wikipedia.org/wiki/List_of_countries_by_population_growth_rate", 1, 0,
             3],
            ["RealPopDensity", "2014",
             "https://en.wikipedia.org/wiki/List_of_countries_by_real_population_density_based_on_food_growing_capacity",
             0, 1, 7],  # 2005,
            ["Urbanization", "2014", "https://en.wikipedia.org/wiki/Urbanization_by_country", 0, 1, 2],  # 2011
            ["GDPPerCapita", "2014", "https://en.wikipedia.org/wiki/List_of_countries_by_distribution_of_wealth", 0, 0,
             8],  # 2000
            ["EmploymentRate", "2014", "https://en.wikipedia.org/wiki/List_of_countries_by_employment_rate", 0, 1, 2],
            # 2013
            # ["MinWage", "2014", "https://en.wikipedia.org/wiki/List_of_minimum_wages_by_country", 0, 0, 3],  # problem
            ["EnergieConsuptionPerAnumPerCapita", "2014",
             "https://en.wikipedia.org/wiki/List_of_countries_by_energy_consumption_per_capita", 0, 0, 4],  # 2013
            ["InternetUsersPercentage", "2014",
             "https://en.wikipedia.org/wiki/List_of_countries_by_number_of_Internet_users", 0, 0, 3],  # 2015
            # ["GreenhouseGasEmission", "2014",
            #  "https://en.wikipedia.org/wiki/List_of_countries_by_greenhouse_gas_emissions_per_capita", 0, 0, 1],
            ["CO2Emission", "2014",
             "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions_per_capita", 1, 1, 23],
            ["Corruption", "2014", "https://en.wikipedia.org/wiki/Global_Corruption_Barometer", 0, 1, 2],
            ["ForestAreaInKm2", "2014", "https://en.wikipedia.org/wiki/List_of_countries_by_forest_area", 1, 0, 1]
        ]

        scrappedData = {}
        scrappedData["labels"] = []
        for label, year, url, index, countryCol, valueCol in params:
            # take in account cases where table is split
            if not scrappedData["labels"] or scrappedData["labels"][-1] != label:
                scrappedData["labels"].append(label)
            newFeatureDict = self.getScrappedFeature(url, index, countryCol, valueCol, year)
            for country, feature in newFeatureDict.items():
                if country in scrappedData:
                    missingNones = (len(scrappedData["labels"]) - 1) - len(scrappedData[country])
                    scrappedData[country] += missingNones * [None] + [feature]
                else:
                    # add missing None's
                    scrappedData[country] = (len(scrappedData["labels"]) - 1) * [None] + [feature]

        print(scrappedData)
        print("Number of features : " + str(len(scrappedData["labels"])))
        return scrappedData
