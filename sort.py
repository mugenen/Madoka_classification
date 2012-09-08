f_list = []
with open('weight', 'r') as f:
    for line in f:
        for feature in line.split():
            f1, f2 = feature.split(':')
            f_list.append((abs(float(f2)), f2, f1))

f_list.sort()
print f_list
