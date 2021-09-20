import os

from docutils.core import publish_parts
from flask import Flask
from flask_flatpages import FlatPages

from applications.misc.constants import BASE_DIR


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False, static_folder=BASE_DIR + '/statics/')
    app.template_folder = '../templates'
    # app.register_error_handler(400, bad_request)
    # app.register_error_handler(401, unauthorized)
    # app.register_error_handler(404, not_found)
    # app.register_error_handler(405, method_not_allowed)
    # app.register_error_handler(500, internal_server_error)

    # admin panel configs
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

    app.config['FLATPAGES_HTML_RENDERER'] = rst_renderer

    #
    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=False)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app


def rst_renderer(text):
    parts = publish_parts(source=text, writer_name='html')
    return parts['fragment']


app = create_app()

pages = FlatPages(app)


from applications.controllers.public import PublicView
from applications.controllers.github_projects import GithubProjectsView
from applications.controllers.visualization import VisualizationView

PublicView.register(app, route_prefix="/")
GithubProjectsView.register(app, route_prefix="/github_projects", name="github")
VisualizationView.register(app, route_prefix="/visualization", name="visualization")

