
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    
    sortedLeft = merge_sort(left)
    sortedRight = merge_sort(right)
    
    return merge(sortedLeft, sortedRight)


def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1 
            
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

    
# nums = [3, 7, 6, -10, 15, 23.5, 55, -13]
# sorted_nums = merge_sort(nums)
# print(sorted_nums)    
    
nums = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(nums)
for i in range(1, n):
    insert_index = i
    current_value = nums.pop(i)
    for j in range (i-1, -1, -1):
        if nums[j] > current_value:
            insert_index = j
        nums.insert(insert_index, current_value)
        
print(nums)
    
