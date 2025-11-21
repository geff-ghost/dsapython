from bst_user_database import TreeMap
class User:
    def __init__(self, username, name, email):
        self.name = name
        self.username = username
        self.email = email
        
    def __repr__(self):
        return "User(username = '{}', name = '{}', email = '{}')".format(self.username, self.name, self.email)
        
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
geff = User('geff', 'Geoffrey Odhiambo', 'geff@example.com')

treemap = TreeMap()
treemap['aakash'] = aakash
treemap['jadhesh'] = jadhesh
treemap['sonaksh'] = sonaksh

treemap['geff'] = geff

treemap.display()

# value = treemap['jadhesh']
# print(value)

for key, value in treemap:
    print(key, value)
    
print(len(treemap))
    