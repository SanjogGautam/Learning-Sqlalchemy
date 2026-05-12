# Filtering/filter_filter_by.py
from main import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
from .filter_filter_by import filter