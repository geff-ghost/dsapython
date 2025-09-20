

tests = []

tests.append({
    'input': {
        'nums': [5, 6, 7, 8, 9, 1, 2, 3, 4],
        'target' : 2
    },
    'output' : 6
})
tests.append({
    'input' :{
        'nums' : [8 ,9, 11, 12, 4, 4, 4,  4, 4, 5, 5, 5],
        'target' : 4
    },
    'output' : 4
})
tests.append({
    'input' :{
        'nums' : [6, 5, 5, 2, 3, 4],
        'target' : 7
    },
    'output' : 0
})
tests.append({
    'input' :{
        'nums' : [7, 8, 9 ,2, 3, 4, 4, 4, 6],
        'target' : 4
    },
    'output' : 5
})
tests.append({
    'input' :{
        'nums' : [7, 8, 9 ,2, 3, 4, 4, 6],
        'target' : 7
    },
    'output' : 0
})
tests.append({
    'input' :{
        'nums' : [7, 8, 9 ,2, 3, 4, 4, 6],
        'target' : 6
    },
    'output' : 7
})
tests.append({
    'input' :{
        'nums' : [6],
        'target' : 6
    },
    'output' : 0
})
tests.append({
    'input' :{
        'nums' : [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'target' : 5
    },
    'output' : 4
})