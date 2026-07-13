# 列表和元组
# 相当于数组
# 列表是可变的，而元组是不可变的
# 在python中列表与元组的元素类型是可变的

# 列表的创建
# 1、使用[]
# 空列表
# a = []
# print(type(a))
#
# # 2、使用list
# b = list()
# print(type(b))
#
# # 3、列表的初始化
# c = [1,2,3]
# print(c)
#
# # 4、不同类型的列表初始化
# d = [1,2,3,'hello','world',2.3,[4,5,6]]
# print(d)
#
# # 5、下标访问
# print(d[0]) # 下标仍然从0开始计算
# print(d[-1]) # python支持负数下标，-1表示倒数最后一个元素，以此类推
# print(d[len(d)-1])


# 列表切片
# a = [1,2,3,4,5,6,7,8,9,0]
# print(a[1:3]) # 打印下标为[1,3)的元素
# print(a[1:])  # 打印从下标1开始的元素
# print(a[:3])  # 打印从下标0开始到下标3之前的元素
# print(a[:-1]) # 打印从下标0开始到倒数第一个之前的元素
# print(a[:])
# print(a[:1000])

# # 列表切片是一个高效的操作，其切出来的片段是原列表里的，而不是通过拷贝实现

# # 切片的步长
# b = [1,2,3,4,5,6,7,8,9,0]
# print(b[1:5:1]) # 顺序走一步
# print(b[::-1])  # 逆序走一步


# 列表的遍历
# a = [1,2,3,4,5]
# for e in a:
#     print(e)
#
# for i in range(0,len(a)):
#     print(a[i])
#
# j = 0
# while j < len(a):
#     a[j] += 10
#     print(a[j])
#     j += 1
# print(a)


# 列表插入元素
# a = [1,2,3,4,5]
# a.append('hello')
# print(a)
#
# a.insert(-1,'world')
# print(a)

# 列表的查找
# in
# a = [1,2,3,4,5]
# print(2 in a)
# print(8 not in a)
#
# # index方法
# print(a.index(2))
# print(a.index(10)) # 不存在则抛异常，不会返回下标

# 列表的删除
# pop
# a = [1,2,3,4,5,6]
# a.pop()
# print(a)
# a.pop(0) # pop的参数还能传下标
# print(a)

# remove按照值来删除
# a = ['aa','bb','cc','dd']
# a.remove('cc')
# print(a)


# 列表的拼接
# + +=
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a+b # 将a与b拼接起来拷贝到c里
# print(c)
#
# a+=b # 等价于 a = a + b 但多了一步把a的旧数据释放的操作
# print(a)
#
# # extend 将b直接拼接到了a后面
# a.extend(b)
# print(a)


# 元组
# a = ()
# print(type(a))
# b = (1,2,3)
# print(b)
# c = (1,2,3,'hello','world')
# print(c)
#
# print(c[1])
# print(c[-1])
# #print(c[100])
#
# d = (1,2,3,4,5,6,7,8,9,0)
# print(d[1:5])
#
# for e in d:
#     print(e)
#
# print(1 in d)
# print(d.index(3))
#
# f = b + c
# print(f)

# 元组只支持读，不支持修改
#a = (1, 2, 3)
# 下面都会异常
# a[0] = 4
# a.pop()
# a.append(1)
# a.extend([1, 2, 3])


# 多元赋值的本质就是用元组的方式来实现的
# def test():
#     x = 1
#     y = 2
#     return x,y
#
# x,y = test()
# print(type(test()))