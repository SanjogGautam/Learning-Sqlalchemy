from sqlalchemy import create_engine, Integer, String, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker, Mapped, mapped_column
from typing import Optional

db_url = "sqlite:///select_in.db"
engine = create_engine(db_url,echo=True)
sessions = sessionmaker(bind=engine)
session = sessions()

class base(DeclarativeBase):
    pass

class User(base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    
    # Use the CLASS NAME 'Posts' here
    latest_post: Mapped[Optional["Posts"]] = relationship('Posts', uselist=False, lazy='selectin')

    def __repr__(self):
        return f'<User {self.name}>'

class Posts(base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))

# Build tables
base.metadata.create_all(engine)

# Seed Data (Checks if empty first to avoid duplicates)
if not session.query(User).first():
    session.add_all([
        User(
            name=f'User_{y}',
            latest_post=Posts(content=f"This is the latest content from User_{y}")
        ) for y in range(100)
    ])
    session.commit()

# Execution
users = session.query(User).all() # This is the "1" in N+1

for user in users:
    # Each access to .latest_post triggers a separate SELECT query
    print(f"{user.name} , {user.latest_post.content}")