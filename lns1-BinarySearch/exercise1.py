# Given an array of integers nums sorted in accending order,
# find the starting and ending index of a given number

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and  nums[mid - 1] == target:
                return 'left'
            else:
                return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums) - 1, condition)

def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)

test = {
    'input': {
        'nums' :[4, 6, 6, 7, 8, 8, 8, 8, 9, 9, 9],
        'target': 8
    },
    'output': [4, 7]
}

first, last = first_and_last_position(**test['input'])
print('First position: {} and Last position: {}'.format(first, last))
