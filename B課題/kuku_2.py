row = int(input("行数を入力して下さい"))
if row <= 0:
    raise ValueError("row <= 0 はエラー")
colum = int(input("列数を入力して下さい"))
if colum <= 0:
    raise ValueError("cloum <= 0 はエラー")
print(''.join(
    [" " + str(y * i) + "\n" if i == 9 else " " + str(y * i) for y in range(1, row + 1) for i in range(1, colum + 1)]))

"""
row = int(input("行数を入力して下さい"))
if row <= 0:
    raise ValueError("row <= 0 はエラー")
colum = int(input("列数を入力して下さい"))
if colum <= 0:
    raise ValueError("cloum <= 0 はエラー")
    
for y in range(1, row + 1):
    print(' '.join([str(i * y) for i in [g for g in range(1, colum + 1)]]))
"""
