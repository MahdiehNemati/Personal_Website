from os import listdir
from os.path import isfile, join

import pandas as pd
import plotly.express as px
from flask import request, render_template
from flask_classful import FlaskView, route


class VisualizationView(FlaskView):
    route_base = "/"

    @route('/')
    def charts(self):
        try:
            x_axis = request.args.get('x_axis')
            y_axis = request.args.get('y_axis')

            df = pd.read_csv('data/country_vaccinations.csv')
            fig = px.bar(df, x=x_axis, y=y_axis, title='Daily Vaccination - Covid 19')
            html_chart = fig.to_html()
            return html_chart
        except Exception as e:
            return "Ther is an Error!"

    @route('/lists')
    def lists(self):
        file_name_list = []
        for f in listdir('data/'):
            # TODO just excel files and formats has to be read.
            if isfile(join('data/', f)) and not f.startswith('.'):
                file_name_list.append(f)

        return render_template('visualization/lists.html', file_name_list=file_name_list)

    @route('/csv_detail/<path_name>')
    def csv_detail(self, path_name):

        return render_template('visualization/csv_detail.html', pepsi=path_name)
