from sqlalchemy.orm import Session
from database import db
from models.production import Production
from datetime import datetime

def save(production_data):
    with Session(db.engine) as session:
        with session.begin():
            new_production = Production(product_id=production_data['product_id'], quantity_produced=production_data['quantity_produced'], date_produced=datetime.now())
            session.add(new_production)
            session.commit()

        session.refresh(new_production)
        return new_production
    
def getAll():
    with Session(db.engine) as session:
        productions = session.query(Production).all()
        print(productions)
        return productions