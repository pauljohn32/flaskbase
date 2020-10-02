from flask import Blueprint

auth_bp = Blueprint('auth_bp',
                     __name__,
                     template_folder='termplates',
                     static_folder='static'
)

from app.auth import routes

