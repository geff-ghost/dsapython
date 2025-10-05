import random

test0 = {
    'input': {
        'nums': [2, 4, 6, 8, 3, 1, 7, 0, 5, 9]
    },
    'output': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
}
test1 = {
    'input': {
        'nums': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 67]
    },
    'output': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 67]
}
test2 = {
    'input': {
        'nums': [9, 9, 9, 6, 6, 3, 3, 1, 1, 1]
    },
    'output': [1, 1, 1, 3, 3, 6, 6, 9, 9, 9]
}
test3 = {
    'input': {
        'nums': []
    },
    'output': []
}
test4 = {
    'input': {
        'nums': [45, 45, 45, 45, 45]
    },
    'output': [45, 45, 45, 45, 45]
}
test5 = {
    'input': {
        'nums': [2]
    },
    'output': [2]
}

in_list = list(range(100000))
out_list = list(range(100000))
random.shuffle(in_list)
test6 = {
    'input': {
        'nums': in_list
    },
    'output' : out_list
}

tests = [test0, test1, test2, test3, test4, test5]

