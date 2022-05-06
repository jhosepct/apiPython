from database.covidDataBase import CovidDataBase

covidDataBase = CovidDataBase()


def reportCovid():
    covidWorld = []
    result = covidDataBase.get_covid()

    for r in result:
        covidWorld.append({
            "country": r[0],
            "totalCases": r[1],
            "newCases": r[2],
            "totalDeaths": r[3],
            "newDeaths": r[4],
            "totalRecovered": r[5],
            "activeCases": r[6],
            "seriousCritical": r[7]
        })
    return covidWorld


def reportCovidContinent():
    covidWorld = []
    result =covidDataBase.get_covid_continent()

    for r in result:
        covidWorld.append({
            "continent": r[0],
            "totalCases": r[1],
            "newCases": r[2],
            "totalDeaths": r[3],
            "newDeaths": r[4],
            "totalRecovered": r[5],
            "activeCases": r[6],
            "seriousCritical": r[7]
        })
    return covidWorld
