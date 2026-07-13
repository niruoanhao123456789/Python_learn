# 在python中的字典其实是一种键值对 key 与 value的映射,相当于c++里的pair
# 在python的字典中存在许多键值对，要求它们具有唯一性

# 字典的创建
# a = {}
# print(type(a))
# b = dict()
# print(type(b))
#
# # 字典的初始化
# d = {
#     "id":123,
#     "name":"zhangsan",
#     "sex":"male"
# } # 最后一个键值的后面的 , 可写与不写
# print(d)
#
# # 字典的查找
# # in
# print("id" in d)
# print('class' in d)
# print(123 in d) # in只用来判定key，与value无关
#
# #[]
# print(d['id'])
# print(d['class']) # 不存在则抛异常

# 对于字典来说，因其实现结构是哈希表，in和[]都是高效的操作
# 对于列表来说，in要对整体进行一次遍历，而[]能实现随机访问


# 字典的插入与修改操作用 []
# a = {
#     'id':123,
#     'name':'zhangsan'
# }
#
# a['class'] = 4 # key值不存在为插入数据
# a['id'] = 1234 # key值存在则修改value
# print(a)
#
# # 字典删除用pop操作
# a.pop('class')
# print(a)
# a.pop('lesson') # 不存在会抛异常


# 字典的遍历
# a = {
#     'id':1234,
#     'class':4,
#     'name':'zhangsan',
#     'age':18
# }
#
# for k in a:
#     print(k)
#
# print(a.keys())
# print(a.values())
# print(a.items())
#
# for k,v in a.items():
#     print(k,v)


# 可hash的值
# print(hash(1))
# print(hash(3.14))
# print(hash('hello'))
# print(hash(True))
# print(hash((1,2,3)))
#
# #print(hash([1,2,3]))
# #一般不可改变的值可以hash