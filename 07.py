# 掷骰子，模拟投掷6千次，计算每个面出现的次数


import random


face1 = 1
face2 = 2
face3 = 3
face4 = 4
face5 = 5
face6 = 6


for i in range(6000):
    # 随机获取（1-6）中的一个数
    range_num = random.randint(1, 6)
    if range_num == 1:
        face1 += 1
        print(f"{range_num}")
    elif range_num == 2:
        face2 += 1
        print(f"{range_num}")
    elif range_num == 3:
        face3 += 1
        print(f"{range_num}")
    elif range_num == 4:
        face4 += 1
        print(f"{range_num}")
    elif range_num == 5:
        face5 += 1
        print(f"{range_num}")
    elif range_num == 6:
        face6 += 1
        print(f"{range_num}")
    else:
        print(f"{range_num}")

# 输出结果值
print(f"1面出现的次数{face1}")
print(f"2面出现的次数{face2}")
print(f"3面出现的次数{face3}")
print(f"4面出现的次数{face4}")
print(f"5面出现的次数{face5}")
print(f"6面出现的次数{face6}")

