import random

test0 = {
    'input':{
        'nums': [8, 5, 3, 9, 1, 2, 0, 4, 7, 6]
    },
    'output': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
}
test1 = {
    'input':{
        'nums': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    },
    'output': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
}
test2 = {
    'input':{
        'nums': [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    },
    'output': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
}
test3 = {
    'input':{
        'nums': [8, 5, 3, 9, 11, 2, 0, 4, 7, 6, 11, 5, 5, 8, 8]
    },
    'output': [0, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 8, 9, 11, 11]
}
test4 = {
    'input':{
        'nums': []
    },
    'output': []
}
test5 = {
    'input':{
        'nums': [8]
    },
    'output': [8]
}
test6 = {
    'input':{
        'nums': [12, 12, 12, 12, 12, 21, 12, 21, 21, 12]
    },
    'output': [12, 12, 12, 12, 12, 12, 12, 21, 21, 21]
}

in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test7 = {
    'input':{
        'nums': in_list
    },
    'output': out_list
}


tests = [test0, test1, test2, test3, test4, test5, test6, test7]
