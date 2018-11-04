
from flask import Flask
# import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
#import dash
import dash


server = Flask(__name__)
# initialize new dash app
app = dash.Dash(__name__, server=server,url_base_pathname='/dashboard/')
# add configurations and database
app.server.config['DEBUG'] = True
app.server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# connect flask_sqlalchemy to the configured flask app

db = SQLAlchemy(app.server)
# from package.models import *
# from dashaltogethernow import dash_layout


from calls.dashboard.dashboard import app
import calls.routes
