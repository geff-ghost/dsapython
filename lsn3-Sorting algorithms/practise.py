#write a function that takes in an array and returns the smallest value

def findSmallest(nums: list[int]):
    if not nums:
        return None  # Return None if the list is empty
    smallest = nums[0]
    for num in nums:
        print(f"num: {num}")
        print(f"smallest: {smallest}")
        print("\n")
        if num < smallest:
            smallest = num
            print(f"smallest: {smallest}")
            print("\n")
    return smallest


nums = [9, 3, 6, 1, 5]
smallest = findSmallest(nums)
print('hello', smallest) 