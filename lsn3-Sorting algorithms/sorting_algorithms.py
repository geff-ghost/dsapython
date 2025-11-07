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

def merge(left, right):
    i, j, merged = 0, 0, []
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    return merge(left_sorted, right_sorted)

def partition(nums, start=0, end=None):
    if end is None:
        end = len(nums)-1
    
    l, r = start, end-1
    
    while r > l:
        # increment the left pointer in number is less or equal to pivot
        if nums[l] <= nums[end]:
            l += 1
        # decrement the right pointer if number is greater than pivot
        elif nums[r] > nums[end]:
            r -= 1
        # two out of place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    
    # place the pivot between the two parts
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end

def quick_sort(nums, start=0, end=None):
    if end is None:
        nums = list(nums)
        end = len(nums)-1
        
    if start < end:
        pivot = partition(nums, start, end)
        quick_sort(nums, start, pivot-1)
        quick_sort(nums, pivot+1, end)
        
    return nums


sorted_arr = quick_sort(test['input']['nums'])

print(f'Unsorted arr: {test["input"]['nums']}')
print(f'Expected output: {test['output']}')
print(f'Actual output: {sorted_arr}')
print('Match: ',sorted_arr == test['output'])
