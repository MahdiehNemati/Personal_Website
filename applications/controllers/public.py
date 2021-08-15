from flask_classful import FlaskView
from flask import render_template


class PublicView(FlaskView):
    route_base = "/"
    def get(self):
        return render_template("/public/index.html")
