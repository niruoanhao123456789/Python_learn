import sys
import os

def menu():
    print('----------------------------------------')
    print('               1. 新增学生')
    print('               2. 删除学生')
    print('               3. 查找学生')
    print('               4. 修改学生信息')
    print('               5. 显示所有学生信息')
    print('               0. 退出')
    print('----------------------------------------')
    choice = int(input('请输入: '))
    return choice

students = []

def Save():
    with open('student.txt','w') as f:
        for student in students:
            f.write(f'{student["id"]}\t{student["name"]}\t{student["classes"]}\t{student["gender"]}\n')
        print('存档成功')

def Load():
    # 如果文件不存在则跳过读档过程
    if not os.path.exists('student.txt'):
        return

    # 读档时先把原有数据进行清理
    global students
    students = []
    with open('student.txt','r',encoding='utf-8') as f:
        for line in f:
            # 对当前行按照\t进行分割前要去除末尾的\n
            line = line.strip() # 能去除一个字符串的首尾的空白符
            tokens = line.split('\t')
            if len(tokens) != 4:
                print(f'当前行存在问题 line:{line}')
                continue
            student = {
                'id': tokens[0],
                'name': tokens[1],
                'classes': tokens[2],
                'gender': tokens[3]
            }
            students.append(student)
    print(f'档成功，共读取了{len(students)}条记录')

def Push():
    print('----------------------------------------')
    print('开始新增学生信息')
    id = input('请输入学号: ')
    name = input('请输入姓名: ')
    classes = input('请输入班级: ')
    gender = input('请输入性别: 1')
    student = {
        'id': id,
        'name': name,
        'classes': classes,
        'gender': gender
    }
    global students
    students.append(student)
    f = open('student.txt', 'a')
    f.write(f'{student["id"]}\t{student["name"]}\t{student["classes"]}\t{student["gender"]}\n')
    f.close()
    print('新增成功')


def Pop():
    print('----------------------------------------')
    id = input('请输入要删除的学生学号: ')
    print('开始删除学生信息')
    for student in students:
        if student['id'] == id:
            students.pop(students.index(student))
            print('删除成功')
            return
    print('删除失败')

def Search():
    print('----------------------------------------')
    name = input('请输入要查找的学生姓名: ')
    print('开始查找学生信息')
    for student in students:
        if student['name'] == name:
            print('查找成功! 学生信息如下:')
            print(f'id: {student["id"]}\tname: {student["name"]}\tclasses: {student["classes"]}\tgender: {student["gender"]}\t\n')
            return
    print('查找失败，该学生不存在')

def ModifyChoice():
    print('开始修改学生信息')
    print('1. 学号 2. 姓名 3. 班级 4. 性别 0. 退出')
    choice = input('请输入: ')
    return int(choice)

def Modify():
    print('----------------------------------------')
    id = input('请输入要修改的学生学号: ')
    for student in students:
        if student['id'] == id:
            while True:
                choice = ModifyChoice()
                if choice == 1:
                    student['name'] = input('请输入新学号: ')
                elif choice == 2:
                    student['name'] = input('请输入新名字: ')
                elif choice == 3:
                    student['classes'] = input('请输入新班级: ')
                elif choice == 4:
                    student['gender'] = input('请输入新型别: ')
                elif choice == 0:
                    break
                else:
                    print('请输入错误，请重新输入')
            print('修改成功')
            Save()
            return
    print('修改失败，该学生不存在')

def Show():
    print('----------------------------------------')
    for student in students:
        print(f'id: {student["id"]}\tname: {student["name"]}\tclasses: {student["classes"]}\tgender: {student["gender"]}\t')


def main():
    Load()
    print('欢迎来到学生管理系统')
    while True:
        choice = menu()
        if choice == 1:
            Push()
        elif choice == 2:
            Pop()
        elif choice == 3:
            Search()
        elif choice == 4:
            Modify()
        elif choice == 5:
            Show()
        elif choice == 0:
            sys.exit(0)
        else:
            print('输入错误，请重新输入')

main()