import requests
from flask import render_template
from flask_classful import FlaskView, route


class GithubProjectsView(FlaskView):
    route_base = "/"

    @route('/<path>')
    def project_detail(self, path):
        github_repo_stars = "https://api.github.com/repos/MahdiehNemati/{path}/stargazers".format(path=path)
        github_stars = requests.get(github_repo_stars)
        if 200 <= github_stars.status_code < 300:
            github_stars = github_stars.json()
            star_numbers = len(github_stars)
        else:
            star_numbers = 0

        github_repo_forks = "https://api.github.com/repos/MahdiehNemati/{path}/forks".format(path=path)
        github_forks = requests.get(github_repo_forks)
        if 200 <= github_forks.status_code < 300:
            github_forks = github_forks.json()
            fork_numbers = len(github_forks)
        else:
            fork_numbers = 0

        return render_template("/github_projects/index.html", path=path, star_numbers=star_numbers,
                               fork_numbers=fork_numbers)
