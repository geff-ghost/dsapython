# the database for all the users

class UserDatabase:
    def __init__(self):
        self.users = []

    def insert_user(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1

        self.users.insert(i, user)


    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
            else:
                return None

    def update_user(self, user):
        target = self.find_user(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users
