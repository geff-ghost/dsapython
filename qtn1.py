# you are given a list of numbers obtained by rotating a sorted
# list an unknown number of times. You are also given a target
# number. Write a function to find the position of the target
# number within the rotated list. You can assume that all the numbers
# in the list are unique
# [5, 6, 9, 0, 2, 3, 4] the target number is 2 and occurs at position
#  5



tests = []

tests.append({
    'input': {
        'nums': [5, 6, 7, 8, 9, 1, 2, 3, 4],
        'target' : 2
    },
    'output' : 6
})
tests.append({
    'input' :{
        'nums' : [8 ,9, 11, 12, 3, 4, 4, 4,  4, 4, 5, 5, 5],
        'target' : 4
    },
    'output' : 5
})
tests.append({
    'input' :{
        'nums' : [6, 5, 5, 2, 3, 4],
        'target' : 7
    },
    'output' : 0
})
tests.append({
    'input' :{
        'nums' : [7, 8, 9 ,2, 3, 4, 4, 4, 6],
        'target' : 4
    },
    'output' : 5
})
tests.append({
    'input' :{
        'nums' : [7, 8, 9 ,2, 3, 4, 4, 6],
        'target' : 7
    },
    'output' : 0
})
tests.append({
    'input' :{
        'nums' : [7, 8, 9 ,2, 3, 4, 4, 6],
        'target' : 6
    },
    'output' : 7
})
tests.append({
    'input' :{
        'nums' : [6],
        'target' : 6
    },
    'output' : 0
})
tests.append({
    'input' :{
        'nums' : [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'target' : 5
    },
    'output' : 4
})

nums = [5, 6, 7, 8, 9, 1, 2, 3, 4, 5]
target = 2
output = 6

def find_element(nums, target):
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = nums[mid]
        print(mid_number)

        if target == mid_number:
            return mid
        elif target < nums[hi]:
            lo = mid + 1

    return 0


# for i in range(len(tests)):
#     nums = tests[i]['input']['nums']
#     target = tests[i]['input']['target']
#     output = tests[i]['output']
#     result = find_element(nums, target)
#     is_correct = result == output

#     print(f'Test {i}: {is_correct} - target: {target}, output: {result}, expected: {output}')

result = find_element(nums, target)
print(f'output: {result}')