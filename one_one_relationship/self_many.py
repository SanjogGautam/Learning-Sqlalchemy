from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
from typing import List, Optional

db_url = "sqlite:///social.db"
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

# 1. The Association Table
class Follower(Base):
    __tablename__ = "followers"
    # Both point to users.id
    follower_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    followed_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)



class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    # 2. Relationship for people I am following
    following: Mapped[List["User"]] = relationship(
        secondary="followers",
        primaryjoin="User.id == Follower.follower_id",
        secondaryjoin="User.id == Follower.followed_id",
        back_populates="followers"
    )

    # 3. Relationship for people following me
    followers: Mapped[List["User"]] = relationship(
        secondary="followers",
        primaryjoin="User.id == Follower.followed_id",
        secondaryjoin="User.id == Follower.follower_id",
        back_populates="following"
    )

Base.metadata.create_all(engine)

# --- Logic Test ---
sanjog = User(name="Sanjog")
sarin = User(name="Sarin")
admin = User(name="Admin")

# Sanjog follows Sarin and Admin
sanjog.following.append(sarin)
sanjog.following.append(admin)

# Sarin follows Sanjog
sarin.following.append(sanjog)

session.add_all([sanjog, sarin, admin])
session.commit()

print(f"Sanjog is following: {[u.name for u in sanjog.following]}")
print(f"Sanjog's followers: {[u.name for u in sanjog.followers]}")