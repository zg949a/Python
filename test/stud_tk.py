import tkinter as tk
#import pickle
#import tkinter.messagebox

root = tk.Tk()
root.title('欢迎登录学生管理系统')
root.geometry('450x300')

canvas = tk.Canvas(root,height=200,width=900)

tk.Label(root,text="用户名").place(x=100,y=150)
tk.Label(root,text="密  码").place(x=100,y=190)


def system():

    info_str ="""
    *******************************
         欢迎使用学生管理系统
    输入1：新建信息
    输入2：显示所有信息
    输入3：查询信息
    输入4：修改信息
    输入5：删除信息
    输入0：退出系统
    输入help：提示信息
    *******************************
    """

    STUD = [
            {'studNo':'2021001', 'name':'John','a':'60','b':'70','c':'80','d':'90','score':'300'}
            ]
    print(info_str)
    while True:
        action = input('请输入想进行的操作： ')
        if action == '0':
            print('\n欢迎再次使用')
            break

        elif action == '1':
            print('\n新建信息')
            studNo = input('输入学号：')
            name = input('输入姓名：')
            a = input('输入a科目成绩：')
            b = input('输入b科目成绩：')
            c = input('输入c科目成绩：')
            d = input('输入d科目成绩：')
            score = int(a) + int(b) + int(c) + int(d)
            stud = {
                    'studNo':studNo,
                    'name':name,
                    'a':a,
                    'b':b,
                    'c':c,
                    'd':d,
                    'score':score
                    }
            STUD.append(stud)

        elif action == '2':
            print('\n显示所有信息')
            for stud in STUD:
                print(stud)

        elif action == '3':
            print('\n查询信息')
            studNo = input('请输入需要查询的学号：eg：2021001 \n')
            for stud in STUD:
                if stud['studNo'] == studNo:
                    print(stud)
                    break
            else:
                print('{}查无此人'.format(studNo))

        elif action == '4':
            print('\n删除信息')
            studNo = input('请输入需要删除信息的学号：eg：2021001 \n')
            for stud in STUD:
                if stud['studNo'] == studNo:
                    STUD.remove(stud)
                    print('删除成功！')
                    break
            else:
                print('{}查无此人'.format(studNo))

        elif action == '5':
            print('\n修改信息')
            studNo = input('请输入需要修改的学号：eg：2021001 \n')
            for stud in STUD:
                if stud['studNo'] == studNo:
                    stud['studNo'] = input('输入新的学号：')
                    stud['name'] = input('输入新的姓名：')
                    stud['a'] = input('输入新的a科目成绩：')
                    stud['b'] = input('输入新的b科目成绩：')
                    stud['c'] = input('输入新的c科目成绩：')
                    stud['d'] = input('输入新的d科目成绩：')
                    stud['score'] = int(stud['a'])+int(stud['b'])+int(stud['c'])+int(stud['d'])
                    break
            else:
                print('{}查无此人'.format(studNo))

        elif action == 'help':
            print(info_str)
        
        else:
            print('输入有误！请重新输入')

root.mainloop()
