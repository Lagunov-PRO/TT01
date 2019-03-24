from flask import Flask
# from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config.from_envvar('RUN_CFG')
# CORS(app)
db = SQLAlchemy(app)
mm = Marshmallow(app)

from . import tasks
app.register_blueprint(tasks.tasks, url_prefix='/tasks')
