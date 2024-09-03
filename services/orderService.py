from sqlalchemy.orm import Session
from sqlalchemy import select
from database import db
from models.order import Order

def save(order_data):
    with Session(db.engine) as session:
        with session.begin():
            new_order = Order(customer_id=order_data['customer_id'], product_id=order_data['product_id'], quantity=order_data['quantity'], total_price=order_data['total_price'])
            session.add(new_order)
            session.commit()

        session.refresh(new_order)
        return new_order
    
def getAll():
    with Session(db.engine) as session:
        orders = session.query(Order).all()
        print(orders)
        return orders
    
def find_all_pagination(page=1, per_page=1):
    orders = db.paginate(select(Order), page=page, per_page=per_page)
    return orders