from flask import render_template, request
import pandas as pd
import plotly.express as px
from flask import render_template
from flask_classful import FlaskView, route


class VisualizationView(FlaskView):
    route_base = "/"

    @route('/')
    def project_detail(self):
        x_axis = request.args.get('x_axis')
        y_axis = request.args.get('y_axis')

        df = pd.read_csv('data/country_vaccinations.csv')
        fig = px.bar(df, x=x_axis, y=y_axis, title='Daily Vaccination - Covid 19')
        html_chart = fig.to_html()
        return html_chart
