
tests = []

tests.append(
    {
        'input': {
            'capacity': 165,
            'weights': [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
            'profits': [92, 57, 49, 68, 60, 43, 67, 84, 84, 72]
        },
        'output': 309
    }
)
tests.append(
    {
        'input': {
            'capacity': 3,
            'weights': [4, 5, 6],
            'profits': [1, 2, 3]
        },
        'output': 0
    }
)
tests.append(
    {
        'input': {
            'capacity': 4,
            'weights': [4, 5, 1],
            'profits': [1, 2, 3]
        },
        'output': 3
    }
)
tests.append(
    {
        'input': {
            'capacity': 170,
            'weights': [41, 50, 49, 59, 55, 57, 60],
            'profits': [442, 525, 511, 593, 546, 564, 617]
        },
        'output': 1735
    }
)
tests.append(
    {
        'input': {
            'capacity': 15,
            'weights': [4, 5, 6],
            'profits': [1, 2, 3]
        },
        'output': 6
    }
)
tests.append(
    {
        'input': {
            'capacity': 15,
            'weights': [4, 5, 1, 3, 2, 5],
            'profits': [2, 3, 1, 5, 4, 7]
        },
        'output': 19
    }
)
