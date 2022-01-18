from models.users import Users

user=Users(username="yuki")
user.save()
print(user.__dict__)
print(user.username, user.lucky_number)


user2=Users(username="ken")
print(user2.username, user2.lucky_number)

print(user.username, user.lucky_number)