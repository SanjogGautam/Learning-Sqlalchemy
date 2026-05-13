from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker,Mapped,mapped_column,DeclarativeBase,relationship
from typing import Optional
db_url="sqlite:///joins.db"
engine=create_engine(db_url,echo=True)
sessions=sessionmaker(bind=engine)
session=sessions()
class base(DeclarativeBase):
    id: Mapped[int]=mapped_column(primary_key=True)

class User(base):
    __tablename__="users"
    name:Mapped[str]=mapped_column()
    age:Mapped[int]=mapped_column()
    address:Mapped[Address]=relationship(uselist=False)
    def __repr__(self):
        return f"{self.name} is {self.age}"
class Address(base):
    __tablename__="addresses"
    address:Mapped[str]=mapped_column()
    user_id:Mapped[Optional[int]]=mapped_column(ForeignKey('users.id'))
    def __repr__(self):
        return f"{self.address}"
base.metadata.drop_all(engine)
base.metadata.create_all(engine)
address1=Address(address="Parbat")
address2=Address(address="Kathmandu")
address3=Address(address="Pokhara")
user1=User(
    name="Sanjog Gautam",
    age=20,
    address=address1
)
user2=User(
    name="Sarin Pradhan",
    age=21,
    address=None
)
session.add_all([address1,address2,address3,user1,user2])
session.commit()