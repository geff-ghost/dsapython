tests = []

tests.append(
    {
        'input': {
            'cards': [15, 12, 10, 9, 7, 5, 3, 2, 0],
            'query': 2
        },
        'output': 7
    }
             )
tests.append(
    {
        'input': {
            'cards': [],
            'query': 7
        },
        'output': -1
    }
             )
tests.append(
    {
        'input': {
            'cards': [15, 12, 10, 9, 7, 5, 3, 2, 0],
            'query': 4
        },
        'output': -1
    }
             )
tests.append(
    {
        'input': {
            'cards': [9, 6, 6, 6, 5, 4, 4, 4, 3, 2, -1, -4, -5],
            'query': 6
        },
        'output': 1
    }
             )
tests.append(
    {
        'input': {
            'cards': [10, 9, 6, 6, 6, 5, 4, 4, 4, 3, 2, -1, -4, -5],
            'query': 10
        },
        'output': 0
    }
             )
tests.append(
    {
        'input': {
            'cards': [10, 9, 6, 6, 6, 5, 4, 4, 4, 3, 2, -1, -4, -5],
            'query': -5
        },
        'output': 13
    }
             )

