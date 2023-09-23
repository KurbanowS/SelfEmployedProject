from flask import Blueprint

bp = Blueprint('dev', __name__)

from main.developers import routes