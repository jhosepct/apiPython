import psycopg2
import pprint

class CovidDataBase:
    #Iniciamos la conexión
    def __init__(self):
        try:
            self.connection=psycopg2.connect(
                "dbname='basededatos' user='postgres' host='localhost' password='********' port='5432'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint("No se pudo conectar a la base de datos")

    def get_covid(self):
        SQL="select country,totalcases,newcases,totaldeaths,newdeaths,totalrecovered,activecases,seriouscritical from covidworld order by totalcases desc"
        self.cursor.execute(SQL)
        return self.cursor.fetchall()
    def get_covid_continent(self):
        SQL="select continent,totalcases,newcases,totaldeaths,newdeaths,totalrecovered,activecases,seriouscritical from covidworldcontinent order by totalcases desc"
        self.cursor.execute(SQL)
        return self.cursor.fetchall()
