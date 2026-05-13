from sqlalchemy import create_engine, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship, sessionmaker, DeclarativeBase
from sqlalchemy.ext.associationproxy import association_proxy, AssociationProxy

engine = create_engine("sqlite://")
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str] = mapped_column(String)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    
    user = relationship("User", back_populates="address")

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    
    # 1. The standard relationship
    address = relationship("Address", back_populates="user", uselist=False)

    # 2. THE ASSOCIATION PROXY
    # Access User.address.city via User.city
    city: AssociationProxy[str] = association_proxy("address", "city")

Base.metadata.create_all(engine)

# --- Usage ---
# You can set the city directly on the User object!
sanjog = User(name="Sanjog", city="Kathmandu") 
session.add(sanjog)
session.commit()

# Even though 'city' is technically in the Address table...
print(f"User Name: {sanjog.name}")
print(f"User City: {sanjog.city}") # Output: Kathmandu