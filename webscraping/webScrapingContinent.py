# encoding: utf-8
import requests
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"


def __number__(str):
    if not str or "N/A".__eq__(str) or "".__eq__(str):
        return 0

    str = str.replace("+", "")
    str = str.replace(",", "")
    str = str.replace(".", "")
    str = str.replace(" ", "")
    str = str.replace('\n', ' ').replace('\r', '')
    if not str:
        return 0
    return int(str)


def reportCovidContinent():
    return reportCovidContinent_webScraping()


def reportCovidContinent_webScraping():
    page_response = requests.get(url, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    page_content2 = page_content.find("table", attrs={"id": "main_table_countries_yesterday"})
    page_content_body = page_content2.find("tbody")
    covidData = []

    covidRows = page_content_body.find_all("tr")
    contPaises = 0
    for row in covidRows[:6]:
        statsHtml = row.find_all("td")
        statsArray = map(lambda data: data.text, statsHtml)
        covidData.append(list(statsArray))

        # name=row.find("a",attrs={"class":"mt_a"}).text
        # name = row.find("a", attrs={"class":"mt_a"}).text

        contPaises += 1

    covidWorld = []
    continent = []
    totalCases = []
    newCases = []
    totalDeaths = []
    newDeaths = []
    totalRecovered = []
    activeCases = []
    seriousCritical = []

    for i in range(contPaises):
        # print(covidData[i])

        nuevoLista = covidData[i]
        continent = nuevoLista[1]
        totalCases = __number__(nuevoLista[2])
        newCases = __number__(nuevoLista[3])
        totalDeaths = __number__(nuevoLista[4])
        newDeaths = __number__(nuevoLista[5])
        totalRecovered = __number__(nuevoLista[6])
        activeCases = __number__(nuevoLista[8])
        seriousCritical = __number__(nuevoLista[9])

        covidWorld.append({
            "continent": continent,
            "totalCases": totalCases,
            "newCases": newCases,
            "totalDeaths": totalDeaths,
            "newDeaths": newDeaths,
            "totalRecovered": totalRecovered,
            "activeCases": activeCases,
            "seriousCritical": seriousCritical
        })

        # print("Country:", country, "| Total Cases:", totalCases, "| New cases:", newCases, "| Total deaths:", totalDeaths
        #    ,"| New Deaths:", newDeaths, "| Total recovered:", totalRecovered, "| Active cases:", activeCases, "| Serious critical:", seriousCritical)
    return covidWorld
