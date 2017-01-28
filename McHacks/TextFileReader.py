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
        #dataCSV['BigEarthCSV'] = []

        for line in contentsBirthRate:
            if not line.strip():
                continue
            else:
                new_contentsBirthRate.append(line.splitlines())

        for line in contentsDeathRate:
            if not line.strip():
                continue
            else:
                new_contentsDeathRate.append(line.splitlines())

        startCountryBirthRate = 0
        startPercentageBirthRate = 7
        startRankBirthRate = 8
        countBirthRate = 11

        startCountryDeathRate = 0
        startPercentageDeathRate = 3
        startRankDeathRate = 4
        countDeathRate = 5


        #if (new_contentsBirthRate[startCountryBirthRate] == new_contentsDeathRate[startCountryDeathRate]):
        dataCSV= {
            'Country': new_contentsBirthRate[startCountryBirthRate],
            'Percentage Birth Rate': new_contentsBirthRate[startPercentageBirthRate],
            'Rank Birth Rate': new_contentsBirthRate[startRankBirthRate]
        }
        #else:
        #    print("The countries are not in a listed order")


        #if (new_contentsBirthRate[startCountryBirthRate] == new_contentsDeathRate[startCountryDeathRate]):
        dataCSV.update({
            'Percentage Death Rate': new_contentsDeathRate[startPercentageDeathRate],
            'Rank Death Rate': new_contentsDeathRate[startRankDeathRate]
        })

        #else:
        #    print("The countries are not in a listed order")

        print (dataCSV)
        print(dataCSV.get('Country'))


        with open('BirthAndDeathRate.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar=',', quoting=csv.QUOTE_ALL)
            spamwriter.writerow(['Country', 'Percentage Birth Rate', 'Rank Birth Rate',
                                 'Percentage Death Rate', 'Rank Death Rate'])
            spamwriter.writerow([dataCSV.get('Country'),
                                dataCSV.get('Percentage Birth Rate'),
                                dataCSV.get('Rank Birth Rate'),
                                dataCSV.get('Percentage Death Rate'),
                                dataCSV.get('Rank Death Rate')])
        '''










'''
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

