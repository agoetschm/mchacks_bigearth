
import csv




def getCountryDict():
	fileOpenBirthRate = open("BirthRate.txt")
	contentsBirthRate = fileOpenBirthRate.readlines()
	fileOpenBirthRate.close()
	fileOpenDeathRate = open("DeathRate.txt")
	contentsDeathRate = fileOpenDeathRate.readlines()
	fileOpenDeathRate.close()

	startCountryBirthRate = 6
	startPercentageBirthRate = 13
	startRankBirthRate = 14
	countBirthRate = 11

	startCountryDeathRate = 6
	startPercentageDeathRate = 9
	startRankDeathRate = 10
	countDeathRate = 5


	# with open (fileOpenBirthRate,"r") as f:
	# 	contentsBirthRate = f.readlines()


	countryList = []
	dictCountry = {}
	for i in range(len(contentsBirthRate)):
		if i+7 >= len(contentsBirthRate):
			break
		if i % countBirthRate == 0:
			countryname = contentsBirthRate[i].strip("\r\n")
			value = contentsBirthRate[i+7].strip("\r\n")
			countryList.append(countryname)
			dictCountry[countryname] = [value]


	for i in range(len(contentsDeathRate)):
		if i+3 >= len(contentsDeathRate):
			break
		if i % countDeathRate == 0:
			countryname = contentsDeathRate[i].strip("\r\n")
			value = contentsDeathRate[i+3].strip("\r\n")
			if countryname in countryList:
				dictCountry[countryname] += [value]
	return dictCountry
# for i in countryList:
# 	print u"{}".format(i)


# printDict (dictCountry)

# def printDict (dictCountry):

# print "{},{}".format(contentsDeathRate[0].strip("\r\n"),contentsDeathRate[7].strip("\r\n"))
# print len (contentsDeathRate)