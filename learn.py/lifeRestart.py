import random
import time
import sys

# welcome界面
print("+----------------------------------------+")
print("\r")
print("           花有重开日,人无再少年")
print("\r")
print("            欢迎来到人生模拟器!")
print("\r")
print("+----------------------------------------+")
print("\r")

# 设置初始属性，总点数不超过20，每项属性点数最大值为10
while True:
    print("请设置初始属性，可用总点数不超过20")
    appearance = int(input("请设置颜值（1-10）: "))
    finances = int(input("请设置家境（1-10）: "))
    physical = int(input("请设置体质（1-10）: "))
    IQ = int(input("请设置IQ(1-10): "))

    if appearance < 1 or appearance > 10:
        print("颜值设置有误")
        continue
    if finances < 1 or finances > 10:
        print("家境设置有误")
        continue
    if physical < 1 or physical > 10:
        print("体质设置有误")
    if IQ < 1 or IQ > 10:
        print("IQ设置有误")
        continue

    print("初始属性输入完毕")
    print(f"颜值:{appearance} ,家境:{finances}, 体质:{physical}, IQ:{IQ}")
    break

# 生成角色性别
# 使用random模块中的randint能生成[begin,end]间的随机数
point = random.randint(1,6)
if point % 2 == 1:
    gender = "female"
    print("你是个女孩")
else:
    gender = "male"
    print("你是个男孩")

# 设置角色出生点
point = random.randint(1,3)
if finances == 10:
    print("你出生在帝都，父母为高管政要")
    finances+=1
    IQ+=1
    physical-=1
elif 6< finances < 10:
    if point == 1:
        print("你出生在大城市，父母为公务员")
        appearance += 2
    elif point == 2:
        print("你出生在大城市，父母为富商")
        finances += 2
    else:
        print("你出生在大城市，父母为学者")
        IQ += 2
elif 3 < finances < 6:
    if point == 1:
        print("你出生在城镇，父母是医生")
        physical += 1
    elif point == 2:
        print("你出生在城镇，父母是教师")
        IQ += 1
    else:
        print("你出生在城镇，父母是商户")
        finances += 1
else:
    if point == 1:
        print("你出生在农村，父母是农民")
        physical += 1
        appearance -= 1
    elif point == 2:
        print("你出生在穷乡僻壤")
        finances -= 1
    else:
        print("你体弱多病")
        physical -= 1
print(f"颜值：{appearance},体质：{physical},智力：{IQ},家境：{finances}")

# 幼年阶段
for age in range(1,11):
    # 把一整年的信息打印到一个字符串中，在这一年的结尾时再统一打印
    infor = f"你今年:{age}岁。"
    # 生成一个[1,3]的随机整数来表示触发的随机事件
    point = random.randint(1,3)
    # 性别触发的事件
    if gender == "female" and finances <= 3 and point == 1:
        infor += "你遇到了重男轻女的家庭，你被遗弃了"
        print(infor)
        print("游戏结束！")
        sys.exit(0)
    # 体质触发的事件
    # 使用elif保证每年只触发一个随机事件
    elif physical < 6 and point == 2:
        infor += "你生了一场大病，"
        physical -= 1
        if finances >= 5:
            infor += "在父母悉心照料下，你康复了"
            physical += 1
            finances -= 1
        else:
            infor += "因无钱医治，你身体情况更糟糕了"
            physical -= 1
    # 颜值触发的事件
    elif appearance <= 4 and age >= 7:
        infor += "你长得太丑，别的小朋友不喜欢你"
        if IQ > 5:
            infor += "你决定用学习来弥补缺点"
            IQ += 1
        else:
            if gender == "male":
                infor += "你因此经常和别人打架"
                physical += 1
                IQ -= 1
            else:
                infor += "你经常被别人欺负"
    # 智商触发的事件
    elif IQ < 5:
        infor += "你看起来不太聪明的样子"
        if finances >= 8 and age >= 6:
            infor += "父母将你送到更好的学校学习"
            IQ += 1
        elif 4 <= finances < 8:
            if gender == "male":
                infor += "父母多鼓励你多运动，争取成为运动员"
                physical += 1
            else:
                infor += "父母鼓励你多注重一下自己的形象"
                appearance += 1
        else:
            # 家境 < 4
            infor += "父母经常因此吵架"
            if point == 1:
                physical -= 1
            elif point == 2:
                IQ -= 1
            else:
                pass
    #健康成长事件
    else:
        infor += "你健康长大"
        physical += 1
        IQ += 1
        appearance += 1

    #打印这一年发生的事件
    print(infor)
    print(f'颜值: {appearance}, 体质: {physical}, 智力: {IQ}, 家境: {finances}')
    print('------------------------------------------------------')
    # 为了方便观察, 加一个小小的暂停操作
    time.sleep(1)