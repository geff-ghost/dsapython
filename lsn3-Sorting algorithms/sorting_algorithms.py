from test_cases import test
from jovian.pythondsa import evaluate_test_case

def bubble_sort(nums: list[int]) -> list[int]:
    nums = list(nums)
    # print('bubble_sort:', nums)

    # repeat the process n-1 times
    for _ in range(len(nums) - 1):
        for i in range(len(nums) - 1):
            # print('i', i, nums[i], nums[i + 1])

            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums

def insertion_sort(nums: list[int]) -> list[int]:
    nums = list(nums)
    for i in range(len(nums)):
        key = nums.pop(i)
        j = i - 1
        while j >= 0 and nums[j] > key:
            j -= 1
        nums.insert(j + 1, key)

    return nums

def merge(nums1: list[int], nums2: list[int]) -> list[int]:
    i, j, merged = 0, 0, []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else: 
            merged.append(nums2[j])
            j += 1

    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]

    return merged + nums1_tail + nums2_tail

def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    sorted_nums = merge(left_sorted, right_sorted)

    return sorted_nums

def partition(nums: list[int], start=0, end=None) -> int:
    # print('partition', nums, start, end)
    if end is None:
        end = len(nums) - 1

    # initialize right and left pointers
    l, r = start, end-1

    # iterate while they're apart
    while r > l:
        # print(' ', nums, l, r)
        # increament left pointer if number is less or equal to pivot
        if nums[l] <= nums[end]:
            l += 1
        # decreament right pointer if number is greater than pivot
        elif nums[r] > nums[end]:
            r -= 1
        # two out-of-place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    
    # print(' ', nums, l, r)
    # place the pivot between the two parts
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end
    
def quick_sort(nums: list[int], start=0, end=None) -> list[int]:
    print('quick_sort', nums, start, end)
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quick_sort(nums, start, pivot-1) #partition before the pivot
        quick_sort(nums, pivot+1, end) #partition after the pivot

    return nums

# nums: list[int] = [1, 5, 4, 2, 0, 11, 3, 44, 7, 12, 6]
# result = quick_sort(nums)
# print(result)

result = evaluate_test_case(merge_sort, test)
