import jovian

def locate_card(cards, query):
    position = 0

    while position < len(cards):
        print('position: ', position, 'cards[position]: ', cards[position])
        if cards[position] == query:
            return position
        position += 1

    return -1

test = {
    'input': {
        'cards': [9, 7, 5, 4, 3, 2, 1, -12],
        'query': -12
    },
    'output': 7
}

print(locate_card(**test['input']) == test['output'])
