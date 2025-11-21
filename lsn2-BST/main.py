from bst_user_profile import User
from bst_user_database import TreeMap

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

treemap = TreeMap()

treemap['aakash'] = aakash
treemap['biraj'] = biraj
treemap['vishal'] = vishal
treemap['siddhant'] = siddhant
treemap['sonaksh'] = sonaksh
treemap['jadhesh'] =jadhesh
treemap['hemanth'] = hemanth

if __name__ == '__main__':

    print('Displaying the Users')
    # displaying the tree
    treemap.display()
    
    # retreiving a value
    print(treemap['jadhesh'].email)
    
    # updating a value
    treemap['jadhesh'] = User(username='jadhesh', name='Jadhesh Aaron', email='jadhesh@new_example')
    print(treemap['jadhesh'].email)
    
    # list of all the values
    print(list(treemap))
    
    # length of the list of users
    print(len(treemap))
    