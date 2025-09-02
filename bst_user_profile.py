# As a senior backend engineer at Jovian, you are tasked with developinng
# a fast in memory data structure to manage profile information(username, name, email)
# for 100 million users. It should allow the following operations to be performed efficiently

# 1. Insert the profile information for a new user
# 2. Find the profile information for a user given there username
# 3. Update the profile information for a user given there username
# 4. List all the users in the platform, sorted by username

# You can assume that usernames are unique
from bst_user_database import UserDatabase


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return "User(username= '{}', name= '{}', email= '{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()
    

# User
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
siddhant = User('siddhant', 'Siddhant Rayaan', 'siddhant@example.com')

database = UserDatabase()

database.insert_user(aakash)
database.insert_user(siddhant)

users = database.list_all()

print(users)


