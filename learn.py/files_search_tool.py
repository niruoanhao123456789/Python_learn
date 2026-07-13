import os

intputPath = input('请输入文件路径:')
pattern = input('请输入文件名或其关键字')

for dirpaths,dirnames,filenames in os.walk(intputPath):
    for f in filenames:
        if pattern in f:
            print(f'{dirpaths}/{f}')