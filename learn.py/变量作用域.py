# x = 10
#
# # 在函数中读取全局变量是可以的，但在函数中会优先寻找局部变量
# def fun1():
#     print(f"x = {x}")
#
# def fun2():
#     x = 20
#     print(f"x = {x}")
#
# # 在函数中使用全局变量用关键字global
# def fun3():
#     global x
#     x+=20
#     print(f"x = {x}")
#
# fun1()
# fun2()
# fun3()

# 在if while for这些代码块不会对变量的作用域产生影响，其定义的变量可以被外部访问
# for i in range(1,11):
#     print(i)
# print("----------------")
# print(i)
#
# if True:
#     x = 10
# print(x)