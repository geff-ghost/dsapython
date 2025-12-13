from jovian.pythondsa import evaluate_test_cases
from knapsack_test_cases import tests

test = {
    'input': {
        'capacity': 15,
        'weights': [4, 5, 1, 3, 2, 5],
        'profits': [2, 3, 1, 5, 4, 7],
        
    },
    'output': 19
}

# knapsack implementation using recursive calls
def max_profits_recursive(weights, profits, capacity, idx=0):
    if idx == len(weights):
        return 0
    elif weights[idx] > capacity:
        return max_profits_recursive(weights, profits, capacity, idx+1)
    else:
        option1 = max_profits_recursive(weights, profits, capacity, idx+1)
        option2 = profits[idx] + max_profits_recursive(weights, profits, capacity-weights[idx], idx+1)

        return max(option1, option2)

evaluate_test_cases(max_profits_recursive, tests)
