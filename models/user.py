from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(db.String(100), nullable=False)
    password: Mapped[str] = mapped_column(db.String(100), nullable=False)
    role: Mapped[str] = mapped_column(db.String(100), nullable=False)