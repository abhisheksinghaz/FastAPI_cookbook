from sqlalchemy.orm import Mapped, mapped_column
from sql_example import database


class User(database.Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]