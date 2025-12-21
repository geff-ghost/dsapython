from jovian.pythondsa import evaluate_test_cases
from test_cases_min_steps import tests

# input
str1 = 'intention'
str2 = 'execution'

# output
output = 4

# recursion
def min_steps(str1: str, str2: str, i1=0, i2=0) -> int:
    if i1 == len(str1):
        return len(str2) - i2
    elif i2 == len(str2):
        return len(str1) - i1
    elif str1[i1] == str2[i2]:
        return min_steps(str1, str2, i1+1, i2+1)
    else:
        return 1 + min(
            min_steps(str1, str2, i1+1, i2),
            min_steps(str1, str2, i1+1, i2+1),
            min_steps(str1, str2, i1, i2+1)
        )


# memorization
def min_steps_memo(str1, str2):
    memo = {}
    def recurse(i1, i2):
        key = i1, i2
        if key in memo:
            return memo[key]
        # if you have exahausted str1
        elif i1 == len(str1):
            return len(str2) - i2
        # if you have exahausted str2
        elif i2 == len(str2):
            return len(str1) - i1
        # if the characters match
        elif str1[i1] == str2[i2]:
            memo[key] = recurse(i1+1, i2+1)
        else:
            memo[key] = 1 + min(
                recurse(i1+1, i2),
                recurse(i1+1, i2+1),
                recurse(i1, i2+1))
        return memo[key]
    return recurse(0, 0)

print(min_steps(str1, str2))
evaluate_test_cases(min_steps_memo, tests)