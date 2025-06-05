# 元组

a = (1,2,3,4)

print(type(a))

print(len(a))

print(1 in a)

for item in a:
    print(item)

a, b, d, e = a
print(a, b, d, e)

# 函数
def add(a, b):
    return a + b