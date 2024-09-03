from flask import Blueprint
from controllers.employeeController import save, getAll

employee_blueprint = Blueprint('employee_bp', __name__)
employee_blueprint.route('/', methods=['POST'])(save)
employee_blueprint.route('/', methods=['GET'])(getAll)