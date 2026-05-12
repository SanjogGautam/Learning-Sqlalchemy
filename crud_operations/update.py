from . import session, User

def update_user_age(name, new_age):
    user = session.query(User).filter_by(name=name).first()
    if user:
        user.age = new_age
        session.commit()
        print(f"Updated {name}'s age to {new_age}")
#filter_by can't do comparison we can also use where(),or_(),and_(),not_()
