import requests
from flask import render_template
from flask_classful import FlaskView


class PublicView(FlaskView):
    route_base = "/"

    def get(self):
        github_url = "https://api.github.com/users/MahdiehNemati/repos"
        github_data = requests.get(github_url)
        github_data = github_data.json()

        return render_template("/public/index.html", github_data=github_data)
