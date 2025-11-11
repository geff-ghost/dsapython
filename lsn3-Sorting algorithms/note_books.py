from final_algorithm import merge_sort

def compare_likes(nb1, nb2):
    if nb1.likes > nb2.likes:
        return 'lesser'
    elif nb1.likes == nb2.likes:
        return 'equal'
    elif nb1.likes < nb2.likes:
        return 'greater'
    
def compare_titles(nb1, nb2):
    if nb1.title < nb2.title:
        return 'lesser'
    elif nb1.title == nb2.title:
        return 'equal'
    elif nb1.title > nb2.title:
        return 'greater'


class Notebook:
    def __init__(self, title, username, likes):
        self.title = title
        self.username = username
        self.likes = likes
        
    def __repr__(self):
        return 'Notebook <"{}/{}", {} likes>'.format(self.username, self.title, self.likes)
    
    
nb0 = Notebook('pytorch_basis', 'aakash', 373)
nb1 = Notebook('linear_regression', 'siddhant', 456)
nb2 = Notebook('logistic_regression', 'vikas', 118)
nb3 = Notebook('feedforward_nn', 'sonaksh', 33)
nb4 = Notebook('cifar10-cnn', 'biraj', 356)
nb5 = Notebook('cifar10-resnet', 'tanya', 21)
nb6 = Notebook('anime-gans', 'hemanth',135 )
nb7 = Notebook('python-fundamentals', 'vishal', 122)
nb8 = Notebook('python-functions', 'aakashns', 213)
nb9 = Notebook('python-numpy', 'siddhant', 98)


notebooks = [nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9]


# sorted_notebooks = merge_sort(notebooks, compare_likes)
sorted_notebooks = merge_sort(notebooks, compare_titles)

for notebook in sorted_notebooks:
    print(notebook)
