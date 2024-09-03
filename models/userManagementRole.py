from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class UserManagementRole(Base):
    __tablename__ = "user_management_roles"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_management_id: Mapped[int] = mapped_column(db.ForeignKey('users.id'))
    role_id: Mapped[int] = mapped_column(db.ForeignKey('roles.id'))