# __init__.py

# Imports
from flask import Flask, render_template
from app.config import Config
from app.models.users import db
from app.routes.auth import authbp

# Initialization...
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

#Register Blueprint
app.register_blueprint(authbp)

#Default Routes
@app.route("/")
def index():
    return render_template("index.html")