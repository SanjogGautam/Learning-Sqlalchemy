from sqlalchemy import create_engine,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, undefer_group ,undefer, sessionmaker, relationship, DeclarativeBase
from typing import Optional,List
db_url="sqlite:///deffered.db"
engine=create_engine(db_url,echo=True)
sessions=sessionmaker(bind=engine)
session=sessions()
class base(DeclarativeBase):
    pass
class User(base):
    __tablename__ = 'users'
    id: Mapped[int]=mapped_column(primary_key=True)
    nick: Mapped[str]=mapped_column(deferred_group="sanjog")
    first_name: Mapped[str]=mapped_column()
    last_name: Mapped[str]=mapped_column(deferred_group="sanjog",deferred_raiseload=True)
    age: Mapped[int]=mapped_column(deferred=True)
    def __repr__(self):
        return f"User: {self.id} - {self.nick}"
session.add(
    User(
        nick="SanjogGT",
        first_name="Sanjog",
        last_name="Gautam",
        age=20
    )
)
base.metadata.create_all(engine)
user=session.query(User).first()
print(user) # User: 1 -
print(user.first_name)
print(user.last_name)
from sqlalchemy.orm import undefer

# Even though 'age' is deferred in the Class definition, 
# this query will fetch it IMMEDIATELY.
user = session.query(User).options(undefer(User.age)).first()

# SQL: SELECT id, nick, first_name, last_name, age FROM users LIMIT 1;
print(user.age) # No extra database hit here!
print(user.age)
# 1. Using undefer_group to fetch nick and last_name at once
# This query will fetch: id, first_name, and the 'sanjog' group (nick, last_name)
user_with_group = session.query(User).options(undefer_group("sanjog")).first()
print("--- Group Eager Loaded ---")
# These will NOT trigger extra SQL because they were fetched together
print(f"Nick: {user_with_group.nick}") 
print(f"Last Name: {user_with_group.last_name}")