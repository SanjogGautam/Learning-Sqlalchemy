from . import session, User

def delete_user(name):
    user = session.query(User).filter_by(name=name).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"Deleted: {name}")