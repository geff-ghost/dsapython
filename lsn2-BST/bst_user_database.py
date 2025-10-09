

class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            # find the first username greater then new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, username):
        target = self.find(username)
        target.name = str(input('update  name: '))
        target.email = str(input('update email: '))

    def list_all(self):
        for user in self.users:
            print(user)
            
