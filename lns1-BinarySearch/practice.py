from test_cases import tests
from jovian.pythondsa import evaluate_test_case

def locate_card(cards, query):
    position = 0

    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1

    return -1

def test_location(mid, cards, query):
    mid_number = cards[mid]
    if mid_number == query:
        if mid-1 >= 0 and cards[mid - 1] == query:
            return 'left'
        return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

def binary_search(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(mid, cards, query)
        
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

large_test = {
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998
}

print('---Linear Search---')
result, passed, runtime = evaluate_test_case(locate_card, large_test, display=False)
print("Result: {}\nPassed: {}\nExecution Time: {} ms".format(result, passed, runtime))

print()

print("---Binary Search--")
result, passed, runtime = evaluate_test_case(binary_search, large_test, display=False)
print("Result: {}\nPassed: {}\nExecution Time: {} ms".format(result, passed, runtime))


