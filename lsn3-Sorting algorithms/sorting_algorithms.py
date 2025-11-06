from tests import tests
test = tests[0]


def bubble_sort(nums: list[int]):
    nums = list(nums)
    n = len(nums)
    
    for i in range(n-1):
        for j in range(n -i -1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                
    return nums

def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i - 1
        while j>=0 and nums[j]>cur:
            j-=1
        nums.insert(j+1, cur)
    
    return nums


sorted_arr = insertion_sort(test['input']['nums'])

print(f'Unsorted arr: {test["input"]['nums']}')
print(f'Expected output: {test['output']}')
print(f'Actual output: {sorted_arr}')
print('Match: ',sorted_arr == test['output'])
