from main import User, engine
from sqlalchemy.orm import sessionmaker

# Common session for all CRUD operations
Session = sessionmaker(bind=engine)
session = Session()

# Hoisting functions from your sub-files (create them below)
from .create import create_user
from .read import get_users
from .update import update_user_age
from .delete import delete_user