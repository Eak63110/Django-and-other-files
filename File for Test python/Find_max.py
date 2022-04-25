x = [1,2,1,3,5,6,4]

max_num = None

for i in x:
    if (max_num is None or i > max_num):
        max_num = i

print('Maximum value:', max_num)
