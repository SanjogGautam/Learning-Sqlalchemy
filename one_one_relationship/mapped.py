from mapped_Model import session,Addresses,User
#creating users
user1=User(name="Sarin Pradhan",email="sarinpradhan@gmail.com")
user2=User(name="Rajesh Kumar",email="Rajeskumar@gmail.com")
#creating addresses
address1=Addresses(city="Kathmandu",state="Bagmati",zip_code=1232)
address2=Addresses(city="Bhaktapur",state="Bagmati",zip_code=1234)
address3=Addresses(city="Lalitpur",state="Bagmati",zip_code=1235)
#associating addresses with users
user1.addresses.extend([address1,address2])
user2.addresses.append(address3)
#adding users to the session and commmiting the changes
session.add(user1)
session.add(user2)
session.commit()

print(f"{user1.addresses= }")
print(f"{user2.addresses= }")
#backward maping:
print(f"{address1.user}")
