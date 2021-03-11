d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}

for key1, value1 in d1.items():
    if key1 in d2:
        d3[key1] = value1 + d2[key1]
    else:
        d3[key1] = value1

for key2, value2 in d2.items():
    if key2 not in d1:
        d3[key2] = value2

print(d3)
