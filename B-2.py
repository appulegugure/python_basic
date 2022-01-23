row = int(input("行数を入力して下さい"))
if row <= 0:
    raise ValueError("row <= 0 はエラー")
colum = int(input("列数を入力して下さい"))
if colum <= 0:
    raise ValueError("cloum <= 0 はエラー")
base = [i * 1 for i in range(1, colum + 1)]
for y in range(1, row + 1):
    result = [i * y for i in base]
    print(' '.join(map(str, result)))
