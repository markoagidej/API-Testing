from flask import Flask
from database import db
from schema import ma
from limiter import limiter
from sqlalchemy.orm import Session

from models.customer import Customer
from models.employee import Employee
from models.order import Order
from models.product import Product
from models.production import Production
from models.user import User
from models.role import Role
from models.userManagementRole import UserManagementRole

from routes.customerBP import customer_blueprint
from routes.employeeBP import employee_blueprint
from routes.orderBP import order_blueprint
from routes.productBP import product_blueprint
from routes.productionBP import production_blueprint
from routes.userBP import user_blueprint

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)

    return app

def blueprint_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(employee_blueprint, url_prefix='/employees')
    app.register_blueprint(order_blueprint, url_prefix='/orders')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(production_blueprint, url_prefix='/productions')
    app.register_blueprint(user_blueprint, url_prefix='/users')

def configure_rate_limit():
    limiter.limit("10/day")(customer_blueprint)
    limiter.limit("10/day")(employee_blueprint)
    limiter.limit("10/day")(order_blueprint)
    limiter.limit("10/day")(product_blueprint)
    limiter.limit("10/day")(production_blueprint)
    limiter.limit("10/day")(user_blueprint)

def init_users_info_data():
    with Session(db.engine) as session:
        with session.begin():
            users = [
                User(username="JDoe", password="JDP", role="admin"),
                User(username="bb", password="bbp", role="user")
            ]
            session.add_all(users)

def init_roles_data():
    with Session(db.engine) as session:
        with session.begin():
            roles = [
                Role(role_name='admin'),
                Role(role_name='user'),
                Role(role_name='guest')
            ]
            session.add_all(roles)

def init_roles_customers_data():
    with Session(db.engine) as session:
        with session.begin():
            roles_users = [
                UserManagementRole(user_management_id=1, role_id=1),
                UserManagementRole(user_management_id=2, role_id=2)
            ]
            session.add_all(roles_users)

if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blueprint_config(app)

    with app.app_context():
        db.drop_all()
        db.create_all()
        init_users_info_data()
        init_roles_data()
        init_roles_customers_data()

    app.run(debug=True)