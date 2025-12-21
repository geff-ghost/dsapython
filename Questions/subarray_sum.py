from jovian.pythondsa import evaluate_test_cases
from test_cases_subarray_sum import tests

li = [1, 7, 4, 2, 1, 3, 11, 5]
target = 10

def subarray_sum1(arr, target):
    n = len(arr)
    # i goes from 0 to n-1
    for i in range(0, n):
        # j goes from i to n
        for j in range(i, n+1):
            if sum(arr[i:j]) == target:
                return i, j

    return None, None

def subarray_sum2(arr, target):
    n = len(arr)
    # i goes from 0 to n-1
    for i in range(0, n):
        s = 0 #running sum

        # j goes from i to n
        for j in range(i, n+1):
            if s == target:
                return i, j
            elif s > target:
                break
            if j < n:
                s += arr[j]
    return None, None

def subarray_sum3(arr, target):
    n = len(arr)
    i, j, s = 0, 0, 0
    while i < n and j < n+1:
        if s == target:
            return i, j
        elif s < target:
            if j < n:
                s += arr[j]
            j += 1
        elif s > target:
            s -= arr[i]
            i += 1
    return None, None


evaluate_test_cases(subarray_sum3, tests)
