from my_password import password as db_password

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://root:{db_password}@localhost/rest_api_design_pattern_db'
    DEBIG = True