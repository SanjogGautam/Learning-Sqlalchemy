from sqlalchemy import create_engine, String
from sqlalchemy.orm import Mapped, mapped_column, undefer_group, sessionmaker, DeclarativeBase, undefer

db_url = "sqlite:///deferred_raiseload.db"
engine = create_engine(db_url, echo=True)
sessions = sessionmaker(bind=engine)
session = sessions()

class base(DeclarativeBase):
    pass

class User(base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    nick: Mapped[str] = mapped_column(deferred_group="sanjog")
    first_name: Mapped[str] = mapped_column()
    
    # --- DEFERRED RAISELOAD ---
    # This column is deferred, AND it is forbidden to lazy-load.
    last_name: Mapped[str] = mapped_column(deferred_group="sanjog", deferred_raiseload=True)
    
    age: Mapped[int] = mapped_column(deferred=True, deferred_raiseload=True)

    def __repr__(self):
        return f"User: {self.id}"

base.metadata.create_all(engine)

# Seed data
if not session.query(User).first():
    session.add(User(nick="SanjogGT", first_name="Sanjog", last_name="Gautam", age=20))
    session.commit()

# --- THE TEST ---
print("\n--- Querying User (age is deferred + raiseload) ---")
user = session.query(User).first()

try:
    print(f"Age: {user.age}") # This will CRASH!
except Exception as e:
    print(f"\n[!] CAUGHT ERROR: {e}")
    print("[!] Why? Because deferred_raiseload=True blocks the automatic second query.")

# --- THE FIX ---
print("\n--- Querying with Explicit Undefer ---")
user_fixed = session.query(User).options(undefer(User.age)).first()
print(f"Fixed Age: {user_fixed.age}") # This works!