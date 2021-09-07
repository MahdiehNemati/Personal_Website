import pandas as pd
from flask_classful import FlaskView

from applications import VaccinationModel
from applications.misc.constants import BASE_DIR


class VaccinationView(FlaskView):
    route_base = "/"

    def get(self):
        csv_data = pd.read_csv(BASE_DIR + '/temp/country_vaccinations.csv')

        for i in csv_data.iterrows():
            VaccinationModel.insert_row(country=i[1].country, iso_code=i[1].iso_code, date=i[1].date)

        return 'ok'
