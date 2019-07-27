from flask import Blueprint

index_blu = Blueprint("tool", __name__)

from . import views
