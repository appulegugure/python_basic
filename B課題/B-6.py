import random


def dice(men_l):
    return random.randint(1, men_l)


men = int(input("サイコロの面の数は？"))
nankai = int(input("何回振りますか？"))
result_containor = []

for i in range(nankai):
    result_containor.append(dice(men))

print(result_containor)
