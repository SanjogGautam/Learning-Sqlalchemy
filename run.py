import crud_operations as crud
import Filtering
# CREATE
crud.create_user("Sanjog Gautam", 20)
crud.create_user("Test User", 99)

# READ
print("\n--- Current Users ---")
for user in crud.get_users():
    print(f"{user.id}: {user.name} ({user.age})")

# UPDATE
crud.update_user_age("Sanjog Gautam", 21)

# DELETE
crud.delete_user("Test User")

#Filter 
Filtering.filter()

print("\nFinal user list:")
for user in crud.get_users():
    print(f"- {user.name}")