import random

in_list = list(range(100000))
out_list = list(range(100000))
random.shuffle(in_list)

# print(in_list[:10])
# print(out_list[:10])

test = {
    'input': {
        'nums': in_list
    },
    'output': out_list
}

tests = [test]
