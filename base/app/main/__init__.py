from flask import Blueprint

main_bp = Blueprint('main', __name__,
                    template_folder="templates",
                    static_folder="static"
)


print("main_bp reached")

from app.main import routes

