from sqlalchemy import create_engine,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base,Mapped,MappedColumn,relationship
from typing import List
db_url="sqlite:///test.db"
engine=create_engine(db_url)
Session=sessionmaker(bind=engine)
session=Session()
base=declarative_base()
class User(base):
    __tablename__='users'
    id:Mapped[int]=MappedColumn(primary_key=True)
    name:Mapped[str]=MappedColumn(String)
    address: Mapped[List["Address"]] = relationship(back_populates="user")
class Address(base):
    __tablename__="addresses"
    id:Mapped[int]=MappedColumn(primary_key=True)
    email:Mapped[str]=MappedColumn(String,unique=True)
    user_id:Mapped[int]=MappedColumn(ForeignKey('users.id'))
    user:Mapped["User"]=relationship(back_populates="address")
base.metadata.create_all(engine) 
newuser=User(name="Sanjog Gautam")
newaddress=Address(email="sanjog@gmail.com",user=newuser)
session.add(newuser)
session.add(newaddress)
session.commit()
print(newuser.name)
print(newaddress.email)
print(newuser.address[0].email)
print(newaddress.user.name)


