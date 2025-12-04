test0 = {
    'input': {
        'seq1': 'serendipitous',
        'seq2': 'precipitation'
    },
    'output': 7
}
test1 = {
    'input': {
        'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
        'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]
    },
    'output': 5
}
test2 = {
    'input': {
        'seq1': 'longest',
        'seq2': 'stone'
    },
    'output': 3
}
test3 = {
    'input': {
        'seq1': 'asdfwevnd',
        'seq2': 'opkpiklklj'
    },
    'output': 0
}
test4 = {
    'input': {
        'seq1': 'densed',
        'seq2': 'condensed'
    },
    'output': 6
}
test5 = {
    'input': {
        'seq1': '',
        'seq2': 'precipitation'
    },
    'output': 0
}
test6 = {
    'input': {
        'seq1': '',
        'seq2': ''
    },
    'output': 0
}
test7 = {
    'input': {
        'seq1': 'abcdef',
        'seq2': 'badcfe'
    },
    'output': 3
}

lcs_tests = [test0, test1, test2, test3, test4, test5, test6,test7]