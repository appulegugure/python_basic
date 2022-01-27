# row入力
row = int(input("行数を入力して下さい"))
if row <= 0:
    raise ValueError("row <= 0 はエラー")

# colum入力
colum = int(input("列数を入力して下さい"))
if colum <= 0:
    raise ValueError("cloum <= 0 はエラー")

# 桁数の最大値計算
row_l = len(str(row))
colum_l = len(str(colum))
max_l = len(str(row * colum)) + 1

# 九九表示
for i in range(1, row + 1):
    for y in range(1, colum + 1):
        print(f"{i: <{row_l}} × {y: <{colum_l}} = {i * y: <{max_l}}|", end='')
    print()

"""
for y in range(1, row + 1):
    print(''.join([f"{int(i) / y:.0f} × {str(y)} = " + i + " | " if len(
        i) > 1 else f"{int(i) / y:.0f} × {str(y)} = " + " " + i + " | " for i in
                      [str(z * y) for z in range(1, colum + 1)]]))
"""
