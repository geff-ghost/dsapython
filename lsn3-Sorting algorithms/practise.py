import random

in_list = list(range(-120, 100))
random.shuffle(in_list)



def findSmallestValue(nums: list[int]):
    minValue = nums[0]
    counter = 1

    while counter < len(nums):
        if minValue > nums[counter]:
            minValue = nums[counter]

        counter += 1

    return minValue

def merge(nums1: list[int], nums2: list[int]):
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


def merge_sort(nums: list[int]):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    sorted_nums = merge(left_sorted, right_sorted)

    return sorted_nums


nums = in_list[:20]
print(nums)

sorted = merge_sort(nums)
print(sorted)
