from flask import render_template
from flask_classful import FlaskView, route


class GithubProjectsView(FlaskView):
    route_base = "/"

    @route('/<path>')
    def project_detail(self, path):
        return render_template("/github_projects/index.html", path=path)
