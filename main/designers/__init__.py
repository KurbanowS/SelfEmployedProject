from flask import Blueprint

bp = Blueprint('des', __name__)

from main.designers import routes