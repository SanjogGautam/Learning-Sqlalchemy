from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,UniqueConstraint
from sqlalchemy.orm import declarative_base,relationship,sessionmaker,Mapped,MappedColumn
db_url="sqlite:///mydb.db"
engine=create_engine(db_url)
Session=sessionmaker(bind=engine)
session=Session()
Base=declarative_base()
class Basemodel(Base):
    __abstract__=True
    __allow_unmapped__=True
    id=Column(Integer,primary_key=True)
class Addresses(Basemodel):
    __tablename__="addresses"
    city=Column(String)
    state=Column(String)
    zip_code=Column(Integer)
   # user_id=Column(ForeignKey("users.id"))
    #user=relationship("User",back_populates="addresses") this is a unmapped way of doing thing
    user_id: Mapped[Integer]=MappedColumn(ForeignKey("user.id"))
    user:Mapped["User"]=relationship(back_populates="addresses")
    def __repr__(self):
        return f"Addresses(city={self.city}, state={self.state}, zip_code={self.zip_code})"
class User(Basemodel):
    __tablename__="users"
    name=Column(String)
    email=Column(String)
    #addresses=relationship("Addresses")
    addresses: Mapped[list["Addresses"]]=relationship()
    def __repr__(self):
        return f"User(name={self.name}, email={self.email})"
Base.metadata.create_all(engine)