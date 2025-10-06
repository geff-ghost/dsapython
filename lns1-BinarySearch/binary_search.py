# final Binary Search algorithm that can be used dynamicaly
from test_cases import tests
from jovian.pythondsa import evaluate_test_cases

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def locate_card(cards, query):

    def condition(mid):
        if cards[mid] == query:
            if mid>0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] > query:
            return 'right'
        elif cards[mid] < query:
            return 'left'
    
    return binary_search(0, len(cards)-1, condition)


result = evaluate_test_cases(locate_card, tests)
