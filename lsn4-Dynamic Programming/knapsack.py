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
        # if the weight is greater than the capacity, we increment idx
        return max_profits_recursive(weights, profits, capacity, idx+1)
    else:
        # we either take the profits or leave it and find the max of the two options
        option1 = max_profits_recursive(weights, profits, capacity, idx+1)
        option2 = profits[idx] + max_profits_recursive(weights, profits, capacity-weights[idx], idx+1)

        return max(option1, option2)


# knapsack implementation using memorization
def max_profits_memo(weights, profits, capacity, idx=0):
    memo = {}
    # this function is called recursively coz the two parameters keep changing
    def recurse(capacity, idx):
        key = (capacity, idx)
        if key in memo:
            return memo[key]
        elif idx == len(weights):
            return 0
        elif weights[idx] > capacity:
            # if weight is greater than capacity we increase the index
            memo[key] = recurse(capacity, idx+1)
        else:
            # we either take the profits or we leave it and find the max of the two options
            option1 = recurse(capacity, idx+1)
            option2 = profits[idx] + recurse(capacity-weights[idx], idx+1)
            memo[key] = max(option1, option2)
        return memo[key]
    return recurse(capacity, idx)


evaluate_test_cases(max_profits_memo, tests)
