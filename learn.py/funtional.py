# 函数
# def 函数名(形参列表):
#   函数体
#   return 返回值
# 其中return根据实际情况可有可无

# 同样遵循先声明定义后调用

# def calSum(begin,end):
#     sum = 0
#     for i in range(begin,end+1):
#         sum += i
#     print(sum)
#
# calSum(1,10)

# 在python中函数能有多个返回值
def getPoint():
    x = 10
    y = 10
    return x,y

# 多元赋值
a,b = getPoint()
print(a)
print(b)

# 如果函数有多个返回值，但我只需要使用其中一部分，不要需要的返回值可以用 _ 来占位
def returnMore():
    x = 10
    y = 20
    z = 30
    return x,y,z

_,a,b = returnMore()
print(a)
print(b)