#!/usr/bin/python3
# root : root
# password : hjkl

def password_check(func):
    def wrapper(*args):
        root = input("请输入用户名：\n")
        tmpw = input("请输入密码：\n")
        if tmpw == 'hjkl' and root == "root":
            print("欢迎使用学生管理系统")
            return func(*args)
        else:
            print("ERROR")
    return wrapper

info_str ="""
*******************************
输入1：新建信息
输入2：显示所有信息
输入3：查询信息
输入4：查询班级最高平均分
输入0：退出系统
输入help：提示信息
*******************************
"""

class Students:
    def __init__(self):
        self.__name = ''
        self.__stud_number = ''
        self.__a_score = 0
        self.__b_score = 0
        self.__c_score = 0
        self.__d_score = 0
    
    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_number(self,number):
        self.__stud_number = number

    def get_number(self):
        return self.__stud_number

    def set_a_score(self,score):
        if score >= 0 and score <= 100 and isinstance(score,(int,float)):
            self.__a_score = score
        else:
            print("输入有误（类型or范围")

    def get_a_score(self):
        return self.__a_score    

    def set_b_score(self,score):
        if score >= 0 and score <= 100 and isinstance(score,(int,float)):
            self.__b_score = score
        else:
            print("输入有误（类型or范围")

    def get_b_score(self):
        return self.__b_score
    
    def set_c_score(self,score):
        if score >= 0 and score <= 100 and isinstance(score,(int,float)):
            self.__c_score = score
        else:
            print("输入有误（类型or范围")

    def get_c_score(self):
        return self.__a_score
    
    def set_d_score(self,score):
        if score >= 0 and score <= 100 and isinstance(score,(int,float)):
            self.__d_score = score
        else:
            print("输入有误（类型or范围")

    def get_d_score(self):
        return self.__d_score

    def get_sum_score(self):
        return sum([self.__a_score, self.__b_score, self.__c_score, self.__d_score])

class Class:
    def __init__(self):
        self.group = []

    def add_stud(self,new):
        self.group.append(new)

    def del_stud(self,del_stud):
        self.group.pop(del_stud)

    def show(self):
        f = open("save.txt","r")
        tem = f.read()
        print(tem)
        f.close()

    def search(self,nu):
        f = open("save.txt","r")
        for line in f:
            if nu in line:
                print(line)
            else:
                print('查无此人')
        f.close()

    def class_avg_max(self):
        studs_sum = []
        for i in self.group:
            studs_sum.append(i.get_sum_score())
        return max(studs_sum)/len(studs_sum)

@password_check
def systemstud():
    print(info_str)
    while True:
        action = input('请输入想要进行的操作：')
        if action == '0':
            print("\n欢迎再次使用")
            break

        elif action == 'help':
            print(info_str)

        elif action == '1':
            print("新建学生信息\n")
            new = Students()
            name = input("输入姓名：")
            new.set_name(name)
            nu = input("输入学号：")
            new.set_number(nu)
            a = float(input("输入a科目成绩："))
            new.set_a_score(a)
            b = float(input("输入b科目成绩："))
            new.set_b_score(b)
            c = float(input("输入c科目成绩："))
            new.set_c_score(c)
            d = float(input("输入d科目成绩："))
            new.set_d_score(d)
            NEW = Class()
            NEW.add_stud(new)
            f = open("save.txt","a")
            f.writelines("姓名:{},学号:{},a科目成绩:{},b科目成绩:{},c科目成绩:{},d科目成绩:{}\n".format(new.get_name(),new.get_number(),new.get_a_score(),new.get_b_score(),new.get_c_score(),new.get_d_score()))
            f.close()
            print("已成功添加：\n姓名{}\t学号{}\ta科目成绩{}\tb科目成绩{}\tc科目成绩{}\td科目成绩{}".format(new.get_name(),new.get_number(),new.get_a_score(),new.get_b_score(),new.get_c_score(),new.get_d_score()))
    
        elif action == '2':
            print("显示所有信息\n")
            NEW = Class()
            NEW.show()

        elif action == '3':
            print("查询信息\n")
            nu = input("输入想要查找的信息：")
            NEW = Class()
            NEW.search(nu)

        elif action == '4':
            print("查询班级最高平均分\n")
            NEW = Class()
            NEW.class_avg_max()

if __name__=="__main__":
    systemstud()
