from model import session,User,Address
#innerjoin
result1=session.query(User).join(Address).all()
print(result1)
#anit-innerjoin
result2=session.query(User).join(Address).filter(Address.user_id==None,User.address==None).all()
print(result2)
#left outer join
result3=session.query(User).join(Address,isouter=True).all()
print(result3)
#left outer join with no common
result4=session.query(User).join(Address,isouter=True).filter(User.address==None).all()
print(result4)
#rigth join
result5=session.query(Address).join(User,isouter=True).all()
print(result5)
#full outer join
result6 = result3+result5
print(result6)