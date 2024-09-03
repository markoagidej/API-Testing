from flask import Blueprint
from controllers.userController import save, getAll, login

user_blueprint = Blueprint('user_bp', __name__)
user_blueprint.route('/', methods=['POST'])(save)
user_blueprint.route('/', methods=['GET'])(getAll)
user_blueprint.route('/login', methods=['POST'])(login)