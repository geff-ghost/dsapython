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


result = evaluate_test_case(merge_sort, test)
