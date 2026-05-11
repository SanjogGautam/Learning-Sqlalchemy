from sqlalchemy import create_engine,Column, Integer, String
from sqlalchemy.orm import declarative_base
# "<dialect>+<driver>://<username>:<password>@<host>:<port>/<database>"
#eg for mysql:
# gg="mysql://<username>:<password>@<host>:<port>/<database>"
#for my sql
url = "sqlite:///database.db"
engine = create_engine(url)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# This creates the table if it doesn't exist
Base.metadata.create_all(engine)