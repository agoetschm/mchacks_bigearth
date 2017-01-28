import csv
class TextFileReader:
    def Reader(self):
        fileOpenBirthRate = open("BirthRate.txt")
        contentsBirthRate = fileOpenBirthRate.readlines()
        fileOpenBirthRate.close()

        fileOpenDeathRate = open("DeathRate.txt")
        contentsDeathRate = fileOpenDeathRate.readlines()
        fileOpenDeathRate.close()

        new_contentsBirthRate = []
        new_contentsDeathRate = []
        dataCSV = {}
        dataCSV['BigEarthCSV'] = []

        for line in new_contentsBirthRate:
            if not line.strip():
                continue
            else:
                new_contentsBirthRate.append(line.splitlines())

        for line in new_contentsDeathRate:
            if not line.strip():
                continue
            else:
                new_contentsDeathRate.append(line.splitlines())

        startCountryBirthRate = 6
        startPercentageBirthRate = 13
        startRankBirthRate = 14
        countBirthRate = 11

        startCountryDeathRate = 6
        startPercentageDeathRate = 9
        startRankDeathRate = 10


        if (new_contentsBirthRate[startCountryBirthRate] == new_contentsDeathRate[startCountryDeathRate]):
            dataCSV['BigEarthCSV'].append({
                'Country': new_contentsBirthRate[startCountryBirthRate],
                'Percentage Birth Rate': new_contentsBirthRate[startPercentageBirthRate],
                'Rank Birth Rate': new_contentsBirthRate[startRankBirthRate],
            })
        else:
            print("The countries are not in a listed order")


        if (new_contentsBirthRate[startCountryBirthRate] == new_contentsDeathRate[startCountryDeathRate]):
            dataCSV['BigEarthCSV'].append({
                'Percentage Death Rate': new_contentsBirthRate[startPercentageBirthRate],
                'Rank Death Rate': new_contentsBirthRate[startRankBirthRate],
            })
        else:
            print("The countries are not in a listed order")










        new_contents = []
        dataPopulation = {}
        dataPopulation['PopulationData'] = []
        for line in contentsBirthRate:
            if not line.strip():
                continue
            else:
                new_contents.append(line.splitlines())

        # print(len(new_contents))

        startCountry = 0
        startRank = 1
        startPopulation = 2
        startDate = 3
        startPercentage = 4
        count = 5

        dataPopulation['PopulationData'].append({
            'Country': new_contents[startCountry],
            'Rank': new_contents[startRank],
            'Population': new_contents[startPopulation],
            'Date': new_contents[startDate],
            'Percentage': new_contents[startPercentage]
        })

        for i in range(47 + 196):
            startCountry += count
            startRank += count
            startPopulation += count
            startDate += count
            startPercentage += count

            dataPopulation['PopulationData'].append({
                'Country': new_contents[startCountry],
                'Rank': new_contents[startRank],
                'Population': new_contents[startPopulation],
                'Date': new_contents[startDate],
                'Percentage': new_contents[startPercentage]
            })

        with open('jsonPopulation.json', 'w') as outfile:
            json.dump(dataPopulation, outfile, indent=4)