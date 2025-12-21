
tests = []

tests.append(
    {
        'input': {
            'arr': [1, 2, 3, 4, 5],
            'target': 9
        },
        'output': (1, 4)
    }
)
tests.append(
    {
        'input': {
            'arr': [10, 2, 3],
            'target': 12
        },
        'output': (0, 2)
    }
)
tests.append(
    {
        'input': {
            'arr': [1, 2, 10],
            'target': 12
        },
        'output': (1, 3)
    }
)
tests.append(
    {
        'input': {
            'arr': [1, 5, 8],
            'target': 5
        },
        'output': (1, 2)
    }
)
tests.append(
    {
        'input': {
            'arr': [1, 0, 2],
            'target': 2
        },
        'output': (1, 3)
    }
)
tests.append(
    {
        'input': {
            'arr': [1, -1, 5, -2],
            'target': 3
        },
        'output': (0, 4)
    }
)
tests.append(
    {
        'input': {
            'arr': [1, 2, 3],
            'target': 10
        },
        'output': (None, None)
    }
)
tests.append(
    {
        'input': {
            'arr': [3, 4, -7, 5],
            'target': 0
        },
        'output': (0, 3)
    }
)


