from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config.from_envvar('RUN_CFG')
db = SQLAlchemy(app)
mm = Marshmallow(app)

from . import projects
app.register_blueprint(projects.projects, url_prefix='/api')

