import requests
from flask import render_template
from flask_classful import FlaskView, route


class GithubProjectsView(FlaskView):
    route_base = "/"

    @route('/<path>')
    def project_detail(self, path):
        github_url = "https://api.github.com/users/MahdiehNemati/repos"
        github_data = requests.get(github_url)
        github_data = github_data.json()

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

        github_repo_branches = "https://api.github.com/repos/MahdiehNemati/{path}/branches".format(path=path)
        github_branches = requests.get(github_repo_branches)
        if 200 <= github_branches.status_code < 300:
            github_branches = github_branches.json()
            branch_numbers = len(github_branches)
        else:
            branch_numbers = 0

        return render_template("/github_projects/detail.html", path=path, star_numbers=star_numbers,
                               fork_numbers=fork_numbers,
                               branch_numbers=branch_numbers, github_data=github_data)
