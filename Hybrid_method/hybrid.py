from sqlalchemy import String, func, create_engine
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)

    @hybrid_property
    def full_name(self):
        # Python-side logic
        return f"{self.first_name} {self.last_name}"

    @full_name.expression
    def full_name(cls):
        # SQL-side logic: Use func.concat for reliability
        return func.concat(cls.first_name, " ", cls.last_name)

    @hybrid_method
    def matches_name(self, name):
        return self.full_name == name

    def __repr__(self):
        return f"<User(name='{self.full_name}')>"

# Setup
engine = create_engine("sqlite:///hybrid.db") 
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()

# Seed Data
session.add(User(first_name="Sanjog", last_name="Gautam"))
session.commit()

# Results
print(f"1. Python: {session.query(User).first().full_name}")
print(f"2. Property Filter: {session.query(User).filter(User.full_name == 'Sanjog Gautam').first()}")
print(f"3. Method Filter: {session.query(User).filter(User.matches_name('Sanjog Gautam')).first()}")