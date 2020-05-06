import os

from flask import Flask

from . import models
from .views import app


models.db.init_app(app)

@app.cli.command("init_db")
def init_db():
    models.init_db()
