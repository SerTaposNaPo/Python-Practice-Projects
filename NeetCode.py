data = [1,2,3,4,4,5,5,5,6]
my_map = {}

for item in data:
    if item not in my_map:
        my_map[item] = 1
    else:
        my_map[item] += 1

print(my_map)