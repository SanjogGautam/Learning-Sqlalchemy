from . import session, User

def get_users():
    return session.query(User).all()