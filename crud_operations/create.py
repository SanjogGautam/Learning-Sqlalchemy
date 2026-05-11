from . import session, User

def create_user(name, age):
    new_user = User(name=name, age=age)
    session.add(new_user)
    session.commit()
    print(f"Created: {name}")