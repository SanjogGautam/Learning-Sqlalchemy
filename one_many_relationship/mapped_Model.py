from typing import List # Required for Mapped[List[...]]
from sqlalchemy import create_engine, String, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

db_url = "sqlite:///mydb.db"
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

# Modern Way: Inherit from DeclarativeBase
class Base(DeclarativeBase):
    pass

class Basemodel(Base):
    __abstract__ = True
    # In 2.0, we use mapped_column instead of Column
    id: Mapped[int] = mapped_column(primary_key=True)

class Addresses(Basemodel):
    __tablename__ = "addresses"
    city: Mapped[str] = mapped_column(String)
    state: Mapped[str] = mapped_column(String)
    zip_code: Mapped[int] = mapped_column(Integer)
    
    # ForeignKey inside mapped_column
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    # Relationship with back_populates
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self):
        return f"Addresses(city={self.city}, state={self.state}, zip_code={self.zip_code})"

class User(Basemodel):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    addresses: Mapped[List["Addresses"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"User(name={self.name}, email={self.email})"

Base.metadata.create_all(engine)