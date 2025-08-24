
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
        'nums' : [6, 6, 6, 6, 6, 5, 5, 4, 3, 8 ,9, 11, 12],
        'target' : 4
    },
    'output' : 7
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
        'nums' : [7, 8, 9 ,2, 3, 4, 4, 6],
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


def find_element(nums, target):
    position = 0

    while position < len(nums):
        if nums[position] == target:
            return position
        
        position += 1

    return 0


for i in range(len(tests)):
    nums = tests[i]['input']['nums']
    target = tests[i]['input']['target']
    output = tests[i]['output']
    result = find_element(nums, target)
    is_correct = result == output

    print(f'Test {i}: {is_correct} - target: {target}, output: {result}, expected: {output}')

# result = find_element(nums, target)
# print(result)