import numpy as np
import pandas as pd

# data = [ 'a' , 'b', 'c' ]
# series = pd.Series(data)
# print(series)


# 索引更换
# data =  [100,101,102,200,201]
# series = pd.Series(data,index=["a","b","c","d","e"])
# print(series)
# print(series[series >= 200])

# 数据更改
# calories = {"day1":1700,"day2":2200,"day3":1900}
# series = pd.Series(calories)
# print(series)
#
# series["day3"]+=200
# print(series)

# DataFrame
# data = {
#     "name": ["John", "Anna", "Michael"],
#     "age": [20, 22, 22]
# }
# # df = pd.DataFrame(data)
# # print(df)
#
# df = pd.DataFrame(data,index=['employee1', 'employee2', 'employee3'])
# # print(df.iloc[0])
# # print(df)
#
# # 增加一列
# df['job'] = ['Cook','N/A','Cashier']
# # print(df)
#
# new_row = pd.DataFrame([{'name': 'Lily','age':22,'job':'Engineer'}],index=['employee4'])
# df = pd.concat([df,new_row])
# print(df)


# import
# csv json
# df = pd.read_csv('data.csv')
# print(df)
#
# df = pd.read_json('data1.json')
# print(df)


# select
# df = pd.read_csv('data.csv')
#
# # select from column
# print(df['name'].to_string())
# print(df[['name','department','city']].to_string())
#
# select from row
# df = pd.read_csv('data.csv',index_col='name')
# print(df.loc['赵敏'])
#
# print(df.loc['张伟':'朱琳',['department','city']])
# print(df.iloc[1:11:2,0:3])
#
# df = pd.read_csv('data.csv',index_col='name')
# while True:
#     employee_name = input('Enter employee name: ')
#     try:
#         print(df.loc[employee_name])
#         print()
#     except KeyError:
#         print(f'{employee_name} not found')
#         print()


# filtering
# df = pd.read_csv('data.csv')
# salary_df = df[df["salary"]>=20000]
# # print(salary_df)
# manager_df = df[(df['is_manager']==True) & (df['bonus']>=6000)]
# print(manager_df)


# 聚合函数
# df = pd.read_csv('data.csv')
# print("mean:")
# print(df.mean(numeric_only=True))
# print("sum:")
# print(df.sum(numeric_only=True))
# print("min:")
# print(df.min(numeric_only=True))
# print("max:")
# print(df.max(numeric_only=True))
# print("count:")
# print(df.count(numeric_only=True))
# print("describe:")
# print(df.describe())

# print('salary mean:')
# print(df["salary"].mean())
# print('salary max:')
# print(df["salary"].max())
# print('salary min:')
# print(df["salary"].min())
# print('salary count:')
# print(df["salary"].count())
# print('salary describe:')
# print(df["salary"].describe())

# group = df.groupby('city')
# print(group['salary'].mean())
# print(group['salary'].median())
# print(group['salary'].min())
# print(group['salary'].max())


# data cleaning
# df = pd.read_csv('data.csv')
#
# # df = df.drop(columns=['is_manager'])
# # print(df.to_string())
#
# # 删除不可用的值
# df = df.dropna(subset=['bonus'])
#
# # 填充不可用的值
# df = df.fillna({"performance_score": "None"})
#
# # 修改
# df['is_manager'] = df['is_manager'].replace({True: "TRUE", False: "FALSE"})
#
# # 统一文本形式
# df['is_manager'] = df['is_manager'].str.lower()
#
# # 去重
# df = df.drop_duplicates()
#
# print(df.to_string())


# 案例
# 1、10人的成绩，数据范围在50-100，计算平均分、最高分、最低分，并筛出高于平均分的学生人数
# np.random.seed(42)
# scores = pd.Series(np.random.randint(50,101,10),index=['学生'+str(i)for i in range(1,11)])
#
# print(scores.to_string())
# print(f'mean: {scores.mean()}')
# print(f'max: {scores.max()}')
# print(f'min: {scores.min()}')
# print(f'others: {scores[scores>scores.mean()]}')
# print(f'nums: {scores[scores>scores.mean()].count()}') # count() 方法只统计有效数值

# 求出温度变化最大的相邻的两天
# temperature = pd.Series([28,31,29,32,30,27,33],index = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
# dif = temperature.diff().abs()
# dif_sort = dif.sort_values()
# print(dif_sort.keys()[:2].to_list())


# 已给出10个交易日的收盘价
# 计算每日收益率（当日收盘价/前日收盘价 - 1）
# 找出收益率最高与最低的日期
# 计算波动率，即收益率的标准差
# prices = pd.Series([102.3,103.5,105.1,104.8,106.2,107.0,106.5,108.1,109.3,110.2]
#                    ,index=pd.date_range('2026-01-01',periods=10))
# profit = prices.pct_change() # 当日收盘价/前日收盘价 - 1
# print(profit)
#
# print(f'max: {profit.idxmax()}')
# print(f'min: {profit.idxmin()}')
# print(f'std: {profit.std()}')


# 已给出某产品过去12个月的销售量
# 计算季度平均销量（每3个月为一季度）
# 找出销量最高的月份
# 计算月环比增长率 （环比指与上个月相比，同比指与往年同期相比）
# 找出连续增长超过2个月的月份
# sales = pd.Series([120,135,145,160,155,170,180,175,190,200,210,220],
#                   index=pd.date_range('2026-01-01', periods=12,freq='ME'))
# # resample 重新采样
# print(sales.resample('QE').mean())
# print(sales.idxmax())
# print(sales.pct_change())
#
# inc = sales.pct_change() > 0
# print(inc[inc.rolling(3).sum() >= 3].keys()) # 滑动窗口函数


# 已给出某商店每小时销售额Series
# 按天来重采样计算每日的总销售额
# 分别计算每天[8:00-22:00]与非该时段的销售比例
# 找出销售额最高的3个小时
# np.random.seed(42)
# hour_sales = pd.Series(np.random.randint(0,100,24),
#                        index=pd.date_range('2026-01-01', periods=24,freq='h'))
#
# day_sales = hour_sales.resample('D').sum()
# business_hour_sales = hour_sales[(hour_sales.index.hour>=8)&(hour_sales.index.hour<=22)].sum()
#
# # hour_sales.between_time('8:00','22:00')
# not_business_hour_sales = hour_sales.drop(hour_sales[(hour_sales.index.hour>=8)&(hour_sales.index.hour<=22)].index).sum()
#
# sales = hour_sales.sort_values(ascending=False)
# print(sales.iloc[0:3])


# 已给出学生的成绩信息
# 计算每位学生的总分和平均分
# 按总分从高到低进行排序，并输出前3名学生
# data = {
#     '姓名': ['zhangsan','lisi','wangwu','zhaoliu','qianqi'],
#     '数学': [85,92,78,88,95],
#     '英语': [90,88,85,92,80],
#     '物理': [75,80,88,85,90]
# }

# 给出某公司销售数据
# 计算每种产品的总销售额（销售额 = 单价 * 销量）
# 找出销售额最高的产品
# 按销售额从高到低排序，并输出所有产品信息
# data = {
#     '产品名': ['a','b','c','d'],
#     '单价': [100,150,200,120],
#     '销量': [50,30,20,40]
# }