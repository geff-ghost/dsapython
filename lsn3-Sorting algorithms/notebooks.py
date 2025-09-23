from merge_sort import merge_sort, compare_likes, compare_titles

class Notebook:
    def __init__(self, title: str, username: str, likes: int):
        self.title, self.username, self.likes = title, username, likes

    def __repr__(self):
        return 'Notebook <"{}/{}", {} likes>'.format(self.username, self.title, self.likes)
    
nb0: Notebook = Notebook('pytorch-basics', 'aakash', 373)
nb1: Notebook = Notebook('linear-regression', 'siddhant', 532)
nb2: Notebook = Notebook('logistic-regression', 'vikas', 31)
nb3: Notebook = Notebook('feedforward-nn', 'sonaksh', 94)
nb4: Notebook = Notebook('cifar10-cnn', 'biraj', 3)
nb5: Notebook = Notebook('cifar10-resnet', 'tanya', 29)
nb6: Notebook = Notebook('anime-gans', 'hemanth', 80)
nb7: Notebook = Notebook('python-fundamentals', 'vishal', 136)
nb8: Notebook = Notebook('python-functions', 'aakashns', 74)
nb9: Notebook = Notebook('python-numpy', 'siddhant', 92)


notebooks: list = [nb0, nb1, nb3, nb4, nb5, nb6, nb7, nb8, nb9]

sorted_notebooks = merge_sort(notebooks, compare_likes)

for decreasing_likes in sorted_notebooks:
    print(f"{decreasing_likes}\n")

# likes = [decreasing_likes for decreasing_likes in sorted_notebooks]
# print(likes)
