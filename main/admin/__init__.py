from flask import Blueprint

bp = Blueprint('AD', __name__)

from main.admin import routes