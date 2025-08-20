
# you are given a list  of numbers obtained by rotating a sorted
# list an unknwon number of times. Write a function to determine the minimum
# number of times the original sorted list was rotated to obtain the given list. 
# Your function should have the worst case  complexity of O(log n), where n is the 
# length of the list. You can assume that all the numbers in the list are unique.
# ie The list [4, 5, 6, 7, 0, 1, 2] is obtained by rotating the sorted list [0, 1, 2, 4, 5, 6, 7] four times.

tests = []

tests.append({
    #the list was rotated 3 times
    "input" : {
        "nums": [4, 5, 6, 7, 0, 1, 2]
    },
    "output": 4
})
tests.append({
    #the list was rotated 3 times
    "input" : {
        "nums": [8, 10, 12, 1 ,0, 1, 2, 4, 5, 6, 7, 5]
    },
    "output": 3
})
tests.append({
    #the list was rotated 3 times
    "input" : {
        "nums": [16, 17, 14, 15, 18, 19 ,4, 5, 6, 7, 9, 10, 13, 15]
    },
    "output": 6
})
tests.append({
    #an empty list
    'input': {
        'nums' : []
    },
    'output' : 0
})
tests.append({
    #the list was rotated once
    "input" : {
        "nums": [8, 0, 2, 4, 5, 6, 7]
    },
    "output": 1
})
tests.append({
    #the list contains repeating numbers
    "input" : {
        "nums": [2, 2, 2, 2, 3, 4, 5, 5, 6, 6, 6]
    },
    "output": 0
})
tests.append({
    #the list was rotated N number of times
    "input" : {
        "nums": [0, 1, 2, 4, 5, 6, 7, 8]
    },
    "output": 0
})
tests.append({
    #the list was rotated n-1 number of times
    "input" : {
        "nums": [1, 2, 4, 5, 6, 7, 0]
    },
    "output": 6
})
tests.append({
    #the list contains just one element
    "input" : {
        "nums": [4]
    },
    "output": 0
})


#nums = [4, 5, 6, 7, 0, 1, 2]

def side_on(lo, hi, mid, nums):
    if nums[mid] < nums[mid - 1]:
        return 'found'
    elif nums[mid] > nums[hi]:
        return 'right'
    else:
        return 'left'
    

def count_rotations_linear(nums):
    lo, hi = 0, len(nums)-1

    while lo <= hi:
        mid = (lo + hi) // 2
        #print(nums[mid])

        side = side_on(lo, hi, mid, nums)
        if side == 'found':
            return mid
        elif side == 'right':
            lo = mid + 1
        elif side == 'left':
            hi = mid - 1
            

    return 0

print("Running tests for count_rotations_linear function...")
# Test all cases at once
for i in range(len(tests)):
    nums = tests[i]['input']['nums']
    expected = tests[i]['output']
    result = count_rotations_linear(nums)
    is_correct = result == expected
    print(f"Test Case {i}: {is_correct} (Got: {result}, Expected: {expected})")
