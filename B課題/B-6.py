import random


def dice(men_l):
    return random.randint(1, men_l)


men = int(input("サイコロの面の数は？"))
nankai = int(input("何回振りますか？"))
result_container = []

for i in range(nankai):
    result_container.append(dice(men))

print(result_container)
