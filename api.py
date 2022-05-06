from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from reporte.reportCovid import get_report_world
from reporte.reportCovid import get_report_continent
app = Flask(__name__) 
CORS(app)
api = Api(app)

class CovidReportWorld(Resource):
    def get(self):
        return get_report_world()

class CovidReportContinent(Resource):
    def get(self):
        return get_report_continent()

api.add_resource(CovidReportWorld, '/world')
api.add_resource(CovidReportContinent, '/continent')
if __name__ == '__main__':
    app.run(debug=True)
