from sqlalchemy import or_, and_ 
from . import User, session

def filter():
    # 1. Exact match (Standard filter_by)
    result1 = session.query(User).filter_by(name='Sanjog Gautam').all()

    # 2. Inequality match (Using the proper != operator)
    result2 = session.query(User).filter(User.name != 'Sanjog Gautam').all()

    # 3. Complex OR logic (Using or_)
    result3 = session.query(User).filter(
        or_(
            User.age > 20,
            User.name == 'Sanjog Gautam'
        )
    ).all()

    # 4. Complex AND logic (Using and_ or multiple where clauses)
    result4 = session.query(User).where(
        and_(
            User.age > 20,
            User.name == 'Sanjog Gautam'
        )
    ).all()

    print(f"Filter_by count: {len(result1)}")
    print(f"Filter (Not Equal) count: {len(result2)}")
    print(f"OR Logic Results: {result3}")
    print(f"AND Logic Results: {result4}")