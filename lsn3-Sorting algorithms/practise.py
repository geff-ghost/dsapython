
def find_minValue(nums):
    minValue = nums[0]
    counter = 0

    while counter < len(nums):
        # print('minValue', minValue)
        if nums[counter] < minValue:
            minValue = nums[counter]
            # print(minValue)
        counter += 1

    return minValue

# nums = []
# value = find_minValue(nums)
# print(value)

num = range(30, 2)
print(num)
