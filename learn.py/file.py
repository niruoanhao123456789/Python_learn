# 文件的打开
# f = open('test.txt','r')
# print(f)
# print(type(f))
#
# # 文件关闭
# f.close()

# GC垃圾回收机制，在python中针对不再使用的资源会进行回收

# 写文件
# f = open('test.txt','w') # 'w'方式打开会覆盖之前写的内容
# f.write('111\n')
# f.close()
#
# f = open('test.txt','a')
# f.write('222')
# f.close()

# 读文件
# 1、read
# f = open('test.txt','r',encoding='utf-8')
# result = f.read(2)
# print(result)
# f.close()

# 2、按行读取
# f = open('test.txt','r',encoding='utf-8')
# # for line in f:
# #     print(f"line={line}")
# for line in f:
#     print(f"line={line}", end='')
# f.close()

# 3、readlines把整个文件的内容都读出来，按行组织到一个列表里
# f = open('test.txt','r',encoding='utf-8')
# lines = f.readlines()
# print(lines)
# f.close()


# # 上下文管理器
# def fun():
#     with open('test.txt','a') as f: #当函数退出时，上下文管理器会自动调用f.close()
#         # ...
#         # ...
#         if True:
#             return
#         # ...
