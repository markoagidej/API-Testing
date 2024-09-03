from sqlalchemy.orm import Session
from sqlalchemy import select
from database import db
from models.user import User
from utils.util import encode_token

def save(user_data):
    with Session(db.engine) as session:
        with session.begin():
            new_user = User(username=user_data['username'], password=user_data['password'], role=user_data['role'])
            session.add(new_user)
            session.commit()

        session.refresh(new_user)
        return new_user
    
def getAll():
    with Session(db.engine) as session:
        users = session.query(User).all()
        print(users)
        return users
    
def login_customer(username, password):
    user = (db.session.execute(db.select(User).where(User.username == username, User.password == password)).scalar_one_or_none())
    role_name = user.role
    if user:
        auth_token = encode_token(user.id, role_name)
        resp = {
            "status": "success",
            "message": "Successfully logged in",
            'auth_token': auth_token
        }
        return resp
    else:
        return None