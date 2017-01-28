from Scrapping import Scrapping
from TextFileReader import TextFileReader

class Main():
    if __name__=="__main__":
        scrappingObj = Scrapping()
        textfilereaderObj = TextFileReader()

        scrappingObj.BirthRate()
        scrappingObj.DeathRate()

        textfilereaderObj.Reader()