from sqlalchemy.orm import Session
from database import db
from models.customer import Customer

def save(customer_data):
    with Session(db.engine) as session:
        with session.begin():
            new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'])
            session.add(new_customer)
            session.commit()

        session.refresh(new_customer)
        return new_customer
    
def getAll():
    with Session(db.engine) as session:
        customers = session.query(Customer).all()
        print(customers)
        return customers