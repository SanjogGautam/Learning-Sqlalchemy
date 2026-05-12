from typing import Optional
from sqlalchemy import String, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

engine = create_engine("sqlite:///self_ref.db")
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    # 1. The Foreign Key points back to the same table's ID
    mentor_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))

    # 2. The "Mentee" side (The one who has a mentor)
    # uselist=False turns this from a list into a single object
    mentor: Mapped[Optional["User"]] = relationship(
        remote_side=[id],      # Tells SQLAlchemy 'id' is the target of the FK
        back_populates="mentee"
    )

    # 3. The "Mentor" side (The one who is mentoring)
    mentee: Mapped[Optional["User"]] = relationship(
        back_populates="mentor",
        uselist=False          # Ensures a mentor can only have ONE mentee
    )

    def __repr__(self):
        return f"<User(name={self.name})>"

Base.metadata.create_all(engine)



sanjog = User(name="Sanjog Gautam")
sarin = User(name="Sarin Pradhan")

# Set the relationship
sarin.mentor = sanjog  # Sanjog is now Sarin's mentor

session.add_all([sanjog, sarin])
session.commit()

print(f"Sarin's Mentor: {sarin.mentor.name}")
print(f"Sanjog's Mentee: {sanjog.mentee.name}")