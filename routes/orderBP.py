from flask import Blueprint
from controllers.orderController import save, getAll, find_all_pagination

order_blueprint = Blueprint('order_bp', __name__)
order_blueprint.route('/', methods=['POST'])(save)
order_blueprint.route('/', methods=['GET'])(getAll)
order_blueprint.route('/paginate', methods=['GET'])(find_all_pagination)