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