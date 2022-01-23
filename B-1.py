"""
for youso1 in range(1, 10):
    for youso2 in range(1, 10):
        print(youso1*youso2, end='')
"""
base = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result_containor = []
for y in range(1, 10):
    result = [i * y for i in base]
    print(' '.join(map(str, result)))
