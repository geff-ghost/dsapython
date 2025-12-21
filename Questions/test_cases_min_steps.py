tests = []

tests.append(
    {
        'input': {
            'str1': 'intention',
            'str2': 'execution'
        },
        'output': 5
    }
)
tests.append(
    {
        'input': {
            'str1': 'execution',
            'str2': 'execution'
        },
        'output': 0
    }
)
tests.append(
    {
        'input': {
            'str1': 'geoffrey',
            'str2': 'execution'
        },
        'output': 8
    }
)
tests.append(
    {
        'input': {
            'str1': '',
            'str2': 'execution'
        },
        'output': 9
    }
)
tests.append(
    {
        'input': {
            'str1': 'geoffrey',
            'str2': ''
        },
        'output': 8
    }
)
tests.append(
    {
        'input': {
            'str1': 'saturday',
            'str2': 'sunday'
        },
        'output': 3
    }
)
