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


# # 在python中函数能有多个返回值
# def getPoint():
#     x = 10
#     y = 10
#     return x,y
#
# # 多元赋值
# a,b = getPoint()
# print(a)
# print(b)
#
# # 如果函数有多个返回值，但我只需要使用其中一部分，不要需要的返回值可以用 _ 来占位
# def returnMore():
#     x = 10
#     y = 20
#     z = 30
#     return x,y,z
#
# _,a,b = returnMore()
# print(a)
# print(b)


# 函数的链式访问 把一个函数的返回值作为另外一个函数的参数使用
# def Add(a,b):
#     return a+b
#
# print(Add(1,2))


# 函数的嵌套使用
# def a():
#     print('a函数调用')
#
# def b():
#     a()
#     print('b函数调用')
#
# def c():
#     b()
#     print('c函数调用')
#
# c()


# 函数的局部变量与函数栈帧
# def Add():
#     num1 = 1
#     num2 = 2
#     return num1 + num2
#
# def cal():
#     num1 = 3
#     print(f'result is :{num1 * Add()}')
#


# 函数递归
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)


# 函数形式参数的默认值
# 参考c++中的缺省值
# 要求函数形参有默认值的话得放在参数列表后面
# def Add(a,b,debug = True):
#     if debug:
#         return a+b
#     else:
#         return 0
#
# print(Add(1,2))


# 函数的关键字
# def test(x,y):
#     print(f'x = {x}, y = {y}')
# # 顺序调用
# test(1,2)
# # 关键字调用
# test(x = 2,y = 3)
# test(y = 4,x = 5)