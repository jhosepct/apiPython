from database.reportCovidWorldDataBase import reportCovid
from webscraping.webScrapingWorld import reportCovidWorld
from database.reportCovidWorldDataBase import reportCovidContinent
from webscraping.webScrapingContinent import reportCovidContinent
FUENTE = "db"
def get_report_world():
    if(FUENTE=="db"):
        return reportCovid()
    elif(FUENTE=="webScraping"):
        return reportCovidWorld()
    else:
        return []

def get_report_continent():
    if (FUENTE == "db"):
        return reportCovidContinent()
    elif (FUENTE == "webScraping"):
        return reportCovidContinent()
    else:
        return []