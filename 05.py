



height = float(input("身高"))
weight = float(input("体重"))


bmi = weight / (height / 100) ** 2

print(f'{bmi = :.1f}')

if 18.5 <= bmi < 24:
    print("正常")
else:
    print("肥胖")

if  bmi >= 24:
    print("肥胖")
elif bmi >= 18.5:
    print("正常")
else:
    print("过轻")



# match

match bmi:
    case 195.0:
        print("正常")
    case 100:
        print("肥胖")
    case _:
        print("过轻")
        