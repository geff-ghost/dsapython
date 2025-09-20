# you are given a list of numbers obtained by rotating a sorted
# list an unknown number of times. You are also given a target
# number. Write a function to find the position of the target
# number within the rotated list. You can assume that all the numbers
# in the list are unique
# [5, 6, 9, 0, 2, 3, 4] the target number is 2 and occurs at position
#  5
from jovian.pythondsa import evaluate_test_cases
from bst_test_cases import tests


def find_element(nums, target):
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            if nums[mid - 1] == target:
                mid = mid - 1
                # return mid
            return mid
        
        # check if the left half is sorted
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            # right half is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1

    return 0


result = evaluate_test_cases(find_element, tests)
