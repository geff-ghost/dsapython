import time as t


nums = [3, 5, 6, 8, 1, 7, 4]

nums.insert(0, 12)


print("Started")
start_time = t.time()
for i in range(100000000):
    j = i * i

end_time = t.time()
print(f'Total time taken: {start_time - end_time}')
print(nums)