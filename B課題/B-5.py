def original_sum(list):
    result = 0
    for i in list:
        result += i
    return result


def original_max(list):
    result = 0
    for i in list:
        if result <= i:
            result = i
    return result


def original_min(list):
    result = 0
    for i in list:
        if result == 0:
            result = i
        elif result >= i:
            result = i
    return result


def original_ave(list):
    result = 0
    for i in list:
        result += i
    return int(result / (len(list) + 1))


if __name__ == '__main__':
    input_data = [int(s) for s in input("データを入力してください").split()]
    gouekei = original_sum(input_data)
    mmaaxx = original_max(input_data)
    mmiinn = original_min(input_data)
    aavvee = original_ave(input_data)

    print(f"合計値：{gouekei}")
    print(f"最大値：{mmaaxx}")
    print(f"最小値：{mmiinn}")
    print(f"平均値：{aavvee:.0f}")
