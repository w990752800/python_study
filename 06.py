# time

import time


# print("xxxx")



# time.sleep(5)


# print("yyyy")



# for in

for i in range(101):
    print(f"{i}")
    time.sleep(2)


# while

while i < 101:
    print(f"{i}")
    time.sleep(2)
    i += 1

# 100以内的素数

# for 循环 range 从 2 到 99
for num in range(2, 100):
    is_prime = True # 声明变量
    for i in range(2, int(num ** 0.5) + 1): # 
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
            print(num)