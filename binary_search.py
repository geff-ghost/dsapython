
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
        "nums": [6, 6, 6, 2, 3, 4, 5, 5, 6]
    },
    "output": 3
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


def count_rotations_linear(nums):
    position = 0

    while position < len(nums)-1:
        if nums[position] > nums[position + 1]:
            return position + 1

        position += 1

    return 0
<<<<<<< HEAD
            
# test_case = 4
# nums = tests[test_case]['input']['nums']
# query = tests[test_case]['output']
# result = count_rotations_linear(nums)
# print(f"Linear Search, test_case {test_case}: output from function {result} == actual output {query} ? {result == query}")



# Test all cases at once
for i in range(len(tests)):
    nums = tests[i]['input']['nums']
    expected = tests[i]['output']
    result = count_rotations_linear(nums)
    is_correct = result == expected
    print(f"Test Case {i}: {is_correct} (Got: {result}, Expected: {expected})")
=======

print("Geff")
test_case = 6
nums = tests[test_case]['input']['nums']
query = tests[test_case]['output']
result = count_rotations_linear(nums)
print(f"Linear Search, test_case {test_case} = {result} == {query} ? {result == query}")
>>>>>>> 0fe359a7bbea918f5a470aa5110c7c32738ea5ff
